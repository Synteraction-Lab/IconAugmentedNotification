package com.hci.nip.android.actuators;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.content.Context;
import android.graphics.Color;
import android.net.Uri;
import android.os.Build;
import android.os.Handler;
import android.os.Looper;
import android.util.Log;
import android.widget.Toast;

import androidx.core.app.NotificationCompat;
import androidx.core.app.NotificationManagerCompat;

import com.hci.nip.android.IntentActionType;
import com.hci.nip.android.actuators.model.NotificationData;
import com.hci.nip.android.service.BroadcastService;
import com.hci.nip.android.service.ErrorCodes;
import com.hci.nip.android.service.ServiceProvider;
import com.hci.nip.base.actuator.Actuator;
import com.hci.nip.base.actuator.ActuatorLocation;
import com.hci.nip.base.actuator.ActuatorType;
import com.hci.nip.base.error.BaseException;
import com.hci.nip.base.error.ErrorCode;
import com.hci.nip.glass.R;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

/**
 * ref: https://developer.android.com/guide/topics/ui/notifiers/toasts#java
 */
public class NotificationActuator extends ServiceProvider implements Actuator {
    private static final String TAG = NotificationActuator.class.getName();

    public static final String CHANNEL_ID = "NOTIFICATION_ACTUATOR_CHANNEL";

    private static final int MAX_NOTIFICATION_DURATION_MILLIS = 10000;
    private final String id;
    private final Context applicationContext;

    private ScheduledExecutorService scheduledExecutorService = null;

    public NotificationActuator(Context appContext, String id) {
        this.id = id;
        this.applicationContext = appContext;

        createNotificationChannel();
    }

    @Override
    public String getId() {
        return id;
    }

    @Override
    public ActuatorType getType() {
        return ActuatorType.ACTUATOR_TYPE_NOTIFIER;
    }

    @Override
    public String getModel() {
        return "vuzix.blade.notification";
    }

    @Override
    public ActuatorLocation getLocation() {
        return ActuatorLocation.ACTUATOR_LOCATION_HEAD;
    }

    @Override
    public String getResolution() {
        return "";
    }

    @Override
    public String getDataFormat() {
        return "message,duration";
    }

    @Override
    public void open() {
        // DO NOTHING
    }

    @Override
    public boolean isActive() {
        return scheduledExecutorService != null;
    }

    @Override
    public void activate() {
        startExecutorService();
    }

    @Override
    public void deactivate() {
        stopExecutorService();
    }

    private void startExecutorService() {
        stopExecutorService();
        scheduledExecutorService = Executors.newSingleThreadScheduledExecutor();
    }

    private void stopExecutorService() {
        if (scheduledExecutorService != null) {
            scheduledExecutorService.shutdownNow();
        }
        scheduledExecutorService = null;
    }

    @Override
    public void close() {
        // DO NOTHING
    }

    @Override
    public boolean processData(List<?> data) {
        Log.d(TAG, "[NotificationActuator] processData");
        if (scheduledExecutorService == null) {
            throw new NotificationActuatorException(ErrorCodes.ACTUATOR_NOT_ACTIVE);
        }

        List<NotificationData> notificationList = getNotificationData(data);
        for (NotificationData notificationData : notificationList) {
            if (notificationData.getWhen() <= 0) {
                scheduledExecutorService.submit(() -> displayNotification(notificationData));
            } else {
                scheduledExecutorService.schedule(() -> displayNotification(notificationData), notificationData.getWhen(), TimeUnit.MILLISECONDS);
            }
        }
        return true;
    }

    /**
     * @param data
     * @return {@link NotificationData}
     * @throws NotificationActuatorException if the data is invalid or empty
     */
    private static List<NotificationData> getNotificationData(List<?> data) {
        if (data == null || data.isEmpty() | !(data.get(0) instanceof NotificationData)) {
            throw new NotificationActuatorException(ErrorCodes.NOTIFICATION_DATA_INVALID);
        }
        List<NotificationData> castedData = new ArrayList<>();
        for (Object dataItem : data) {
            castedData.add((NotificationData) dataItem);
        }
        return castedData;
    }

    public void displayNotification(NotificationData notification) {
        Log.d(TAG, "[NOTIFICATION] showMessage:" + notification);
        switch (notification.getType()) {
            case NotificationData.TYPE_HEADS_UP:
                displayHeadsUpNotification(notification);
                break;
            case NotificationData.TYPE_CUSTOM:
                displayCustomNotification(notification);
                break;
            case NotificationData.TYPE_TOAST:
            default:
                displayToastNotification(notification);
                break;
        }
    }

    private void displayToastNotification(NotificationData notification) {
        long duration = notification.getDuration();
        int displayTime;
        if (duration <= 0) {
            displayTime = Toast.LENGTH_SHORT;
        } else if (duration < MAX_NOTIFICATION_DURATION_MILLIS) {
            displayTime = (int) duration;
        } else {
            displayTime = MAX_NOTIFICATION_DURATION_MILLIS;
        }

        Handler handler = new Handler(Looper.getMainLooper());
        handler.post(() -> {
            // toast.setGravity(Gravity.TOP|Gravity.LEFT, 0, 0);
            Toast.makeText(applicationContext, notification.getMessage(), displayTime).show();
        });
    }

    private void createNotificationChannel() {
        Log.d(TAG, "[NOTIFICATION] createNotificationChannel");
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            NotificationChannel serviceChannel = new NotificationChannel(CHANNEL_ID, "Notification Actuator Channel", NotificationManager.IMPORTANCE_HIGH);
            serviceChannel.setShowBadge(true);
            serviceChannel.enableLights(true);
            serviceChannel.setLockscreenVisibility(Notification.VISIBILITY_PUBLIC);

            NotificationManagerCompat notificationManager = NotificationManagerCompat.from(this.applicationContext);
            notificationManager.createNotificationChannel(serviceChannel);
        }
    }

    private void displayHeadsUpNotification(NotificationData notificationData) {
        NotificationCompat.Builder notificationBuilder = new NotificationCompat.Builder(this.applicationContext, CHANNEL_ID)
                .setTicker(notificationData.getTitle()) // for accessibility
                .setContentTitle(notificationData.getTitle())
                .setContentText(notificationData.getMessage())
                .setPriority(notificationData.getPriority())
                .setAutoCancel(true)
                .setCategory(Notification.CATEGORY_EVENT)
                .setVisibility(NotificationCompat.VISIBILITY_PUBLIC);

        // see https://stackoverflow.com/questions/16055073/set-drawable-or-bitmap-as-icon-in-notification-in-android
        // see https://github.com/google/material-design-icons
        ColorText icon = getColorText(notificationData.getSmallIcon());
        String icon_name = icon.getText();
        if (icon_name != null && !icon_name.isEmpty()) {
            notificationBuilder.setSmallIcon(NotificationIconMapping.getIcon(icon_name));
        }

        Log.d(TAG, "TICON: " + icon + ", notif" + notificationBuilder.build());
        if (icon.getColor() != 0) {
            notificationBuilder.setColor(icon.getColor());
        }

        if (notificationData.isBigTextEnable()) {
            notificationBuilder.setStyle(new NotificationCompat.BigTextStyle().bigText(notificationData.getMessage()));
        }

        int notificationDefaults = 0;
        if (notificationData.isLightsEnable()) {
            notificationDefaults |= NotificationCompat.DEFAULT_LIGHTS;
        }
        if (notificationData.isSoundEnable()) {
            notificationDefaults |= NotificationCompat.DEFAULT_SOUND;
        }
        if (notificationData.isVibrationEnable()) {
            notificationDefaults |= NotificationCompat.DEFAULT_VIBRATE;
        }
        notificationBuilder.setDefaults(notificationDefaults);

        if (notificationData.isLightsEnable()) {
            notificationBuilder.setLights(Color.BLUE, 500, 500);
        }
        if (notificationData.isSoundEnable()) {
            //  see https://stackoverflow.com/questions/15809399/android-notification-sound, https://stackoverflow.com/questions/11271991/uri-to-default-sound-notification
//            notificationBuilder.setSound(Settings.System.DEFAULT_NOTIFICATION_URI);
            notificationBuilder.setSound(Uri.parse("android.resource://" + this.applicationContext.getPackageName() + "/" + R.raw.cake));
        }
        if (notificationData.isVibrationEnable()) {
            notificationBuilder.setVibrate(new long[]{500, 500, 500, 0, 0});
        }

        int uniqueNotificationId = (int) System.currentTimeMillis();

        Handler handler = new Handler(Looper.getMainLooper());
        handler.post(() -> {
            NotificationManagerCompat notificationManager = NotificationManagerCompat.from(this.applicationContext);
            notificationManager.notify(uniqueNotificationId, notificationBuilder.build());
        });
    }

    private void displayCustomNotification(NotificationData notification) {
        Log.d(TAG, "Custom Notification: " + notification);
        Long uniqueKey = dataRepository.getUniqueKey();
        dataRepository.addRequest(uniqueKey, notification);
        // TODO: wait until completed
        broadcastService.sendBroadcast(BroadcastService.getBroadcastIntent(IntentActionType.NOTIFICATION_UPDATE, uniqueKey));
    }


    public static class NotificationIconMapping {
        private static HashMap<String, Integer> nameIconMap = null;

        public static int getIcon(String iconName) {
            if (nameIconMap == null) {
                nameIconMap = new HashMap<>();

                nameIconMap.put("acc", R.drawable.ic_acc_notif);
                nameIconMap.put("alarm", R.drawable.ic_alarm_notif);
                nameIconMap.put("amazon", R.drawable.ic_amazon_notif);
                nameIconMap.put("archive", R.drawable.ic_archive_notif);
                nameIconMap.put("backup", R.drawable.ic_backup_notif);
                nameIconMap.put("battery", R.drawable.ic_battery_notif);
                nameIconMap.put("battery_low", R.drawable.ic_battery_10_notif);
                nameIconMap.put("bug", R.drawable.ic_bug_notif);
                nameIconMap.put("call", R.drawable.ic_call_notif);
                nameIconMap.put("camera", R.drawable.ic_camera_notif);
                nameIconMap.put("cart", R.drawable.ic_cart_notif);
                nameIconMap.put("calendar", R.drawable.ic_calendar_notif);
                nameIconMap.put("cash", R.drawable.ic_cash_notif);
                nameIconMap.put("chat", R.drawable.ic_chat_notif);
                nameIconMap.put("error", R.drawable.ic_error_notif);
                nameIconMap.put("email", R.drawable.ic_email_notif);
                nameIconMap.put("gmail", R.drawable.ic_gmail_notif);
                nameIconMap.put("facebook", R.drawable.ic_facebook_notif);
                nameIconMap.put("google_drive", R.drawable.ic_google_drive_notif);
                nameIconMap.put("google_play", R.drawable.ic_google_play_notif);
                nameIconMap.put("instagram", R.drawable.ic_instagram_notif);
                nameIconMap.put("news", R.drawable.ic_news_notif);
                nameIconMap.put("settings", R.drawable.ic_settings_notif);
                nameIconMap.put("skype", R.drawable.ic_skype_notif);
                nameIconMap.put("whatsapp", R.drawable.ic_whatsapp_notif);
                nameIconMap.put("youtube", R.drawable.ic_youtube_notif);
                nameIconMap.put("app", R.drawable.ic_priority_notif);
                nameIconMap.put("google", R.drawable.ic_google_notif);
                nameIconMap.put("twitter", R.drawable.ic_twitter_notif);
                nameIconMap.put("hangout", R.drawable.ic_hangouts_notif);
                nameIconMap.put("snapchat", R.drawable.ic_snapchat_notif);
                nameIconMap.put("evernote", R.drawable.ic_evernote_notif);
                nameIconMap.put("apple", R.drawable.ic_apple_notif);
                nameIconMap.put("battery50", R.drawable.ic_battery_50_notif);

                nameIconMap.put("img_meeting", R.drawable.img_meeting);
                nameIconMap.put("img_doctor", R.drawable.img_doctor);
                nameIconMap.put("img_delivery", R.drawable.img_delivery);
                nameIconMap.put("img_birthday", R.drawable.img_birthday);
                nameIconMap.put("img_lunch", R.drawable.img_lunch);
                nameIconMap.put("img_meet", R.drawable.img_meet);
                nameIconMap.put("img_turn_left", R.drawable.img_turn_left);
                nameIconMap.put("img_whatsapp", R.drawable.img_whatsapp);
                nameIconMap.put("img_yoga", R.drawable.img_yoga);
                nameIconMap.put("img_transaction", R.drawable.img_transaction);
                nameIconMap.put("img_backup", R.drawable.img_backup);
                nameIconMap.put("img_backup_computer", R.drawable.img_backup_computer);
                nameIconMap.put("img_backup_computer2", R.drawable.img_backup_computer2);
                nameIconMap.put("img_backup_computer3", R.drawable.img_backup_computer3);
                nameIconMap.put("img_credit_card", R.drawable.img_credit_card);
                nameIconMap.put("img_credit_card2", R.drawable.img_credit_card2);
                nameIconMap.put("img_theater", R.drawable.img_theater);
                nameIconMap.put("img_movie", R.drawable.img_movie);
                nameIconMap.put("img_today", R.drawable.img_today);
                nameIconMap.put("img_pin", R.drawable.img_pin);
                nameIconMap.put("img_send", R.drawable.img_send);
                nameIconMap.put("img_forward", R.drawable.img_forward);
                nameIconMap.put("img_reply", R.drawable.img_reply);
                nameIconMap.put("img_plane", R.drawable.img_plane);
                nameIconMap.put("img_plane_status", R.drawable.img_plane_status);
                nameIconMap.put("img_computer", R.drawable.img_computer);
                nameIconMap.put("img_bus_departure", R.drawable.img_bus_departure);
                nameIconMap.put("img_cycling", R.drawable.img_cycling);
                nameIconMap.put("img_coffee", R.drawable.img_coffee);
                nameIconMap.put("img_taxi", R.drawable.img_taxi);
                nameIconMap.put("img_cash", R.drawable.img_cash);
                nameIconMap.put("img_pay_cash", R.drawable.img_pay_cash);
                nameIconMap.put("img_pay_cash2", R.drawable.img_pay_cash2);
                nameIconMap.put("img_payment", R.drawable.img_payment);
                nameIconMap.put("img_pay_mobile", R.drawable.img_pay_mobile);
                nameIconMap.put("img_visitor", R.drawable.img_visitor);
                nameIconMap.put("img_leave", R.drawable.img_leave);
                nameIconMap.put("img_mom_day", R.drawable.img_mom_day);
                nameIconMap.put("img_valentine_day", R.drawable.img_valentine_day);
                nameIconMap.put("img_pay_rent", R.drawable.img_pay_rent);
                nameIconMap.put("img_pay_rent2", R.drawable.img_pay_rent2);
                nameIconMap.put("img_send_presentation", R.drawable.img_send_presentation);
                nameIconMap.put("img_presentation", R.drawable.img_presentation);
                nameIconMap.put("img_presentation2", R.drawable.img_presentation2);
                nameIconMap.put("img_shop_milk_eggs", R.drawable.img_shop_milk_eggs);
                nameIconMap.put("img_milk_eggs", R.drawable.img_milk_eggs);
                nameIconMap.put("img_add_shopping", R.drawable.img_add_shopping);
                nameIconMap.put("img_ticket", R.drawable.img_ticket);
                nameIconMap.put("img_standup", R.drawable.img_standup);
                nameIconMap.put("img_standing", R.drawable.img_standing);
                nameIconMap.put("img_id_card", R.drawable.img_id_card);
                nameIconMap.put("img_licence", R.drawable.img_license);
                nameIconMap.put("img_licence2", R.drawable.img_license2);
                nameIconMap.put("img_exercise_stretch", R.drawable.img_exercise_stretch);
                nameIconMap.put("img_exercise_gym", R.drawable.img_exercise_gym);
                nameIconMap.put("img_delete", R.drawable.img_delete);
                nameIconMap.put("img_update_phone", R.drawable.img_update_phone);
                nameIconMap.put("img_order_online", R.drawable.img_order_online);
                nameIconMap.put("img_topup_cash", R.drawable.img_topup_cash);
                nameIconMap.put("img_sync_photos", R.drawable.img_sync_photos);
                nameIconMap.put("img_take_photo", R.drawable.img_take_photo);
                nameIconMap.put("img_download", R.drawable.img_download);
                nameIconMap.put("img_cleaning", R.drawable.img_cleaning);


            }

            Integer iconVal = nameIconMap.get(iconName);
            if (iconVal == null) {
                return 0;
            } else {
                return iconVal;
            }
        }
    }

    public static class NotificationActuatorException extends BaseException {
        public NotificationActuatorException(ErrorCode errorCode) {
            super(errorCode);
        }
    }

    public static class ColorText {
        private final int color;
        private final String text;

        public ColorText(int color, String text) {
            this.color = color;
            this.text = text;
        }

        public int getColor() {
            return color;
        }

        public String getText() {
            return text;
        }

        @Override
        public String toString() {
            return "ColorText{" +
                    "color=" + color +
                    ", text='" + text + '\'' +
                    '}';
        }
    }

    public static int getColor(String s) {
        try {
            return Color.parseColor(s);
        } catch (Exception e) {
            return Color.TRANSPARENT;
        }
    }

    /**
     * @param colorAndText format: <#argb> <text>  OR <text>
     * @return #ColorText
     */
    public static ColorText getColorText(String colorAndText) {
        if (colorAndText == null || colorAndText.isEmpty() || colorAndText.charAt(0) != '#' || colorAndText.length() <= 10) {
            return new ColorText(0, colorAndText);
        } else {
            return new ColorText(getColor(colorAndText.substring(0, 9)), colorAndText.substring(10));
        }
    }
}
