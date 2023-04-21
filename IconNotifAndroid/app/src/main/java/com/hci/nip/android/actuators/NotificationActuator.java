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

                nameIconMap.put("img_whatsapp", R.drawable.img_whatsapp);
                nameIconMap.put("img_theater", R.drawable.img_theater);
                nameIconMap.put("img_today", R.drawable.img_today);
                nameIconMap.put("img_computer", R.drawable.img_computer);
                nameIconMap.put("img_cash", R.drawable.img_cash);
                nameIconMap.put("img_cash1", R.drawable.img_cash2);
                nameIconMap.put("img_payment", R.drawable.img_payment);
                nameIconMap.put("img_update_phone", R.drawable.img_update_phone);

                nameIconMap.put("img_message2", R.drawable.img_message2);
                nameIconMap.put("img_message4", R.drawable.ic_chat_notif);
                nameIconMap.put("img_meet4", R.drawable.img_meet4);
                nameIconMap.put("img_pin4", R.drawable.img_pin4);
                nameIconMap.put("img_send4", R.drawable.img_send4);
                nameIconMap.put("img_forward2", R.drawable.img_forward2);
                nameIconMap.put("img_forward4", R.drawable.img_forward4);
                nameIconMap.put("img_cleaning1", R.drawable.img_cleaning1);
                nameIconMap.put("img_cleaning4", R.drawable.img_cleaning4);
                nameIconMap.put("img_yoga1", R.drawable.img_yoga1);
                nameIconMap.put("img_yoga2", R.drawable.img_yoga2);
                nameIconMap.put("img_yoga4", R.drawable.img_yoga4);
                nameIconMap.put("img_cycling1", R.drawable.img_cycling1);
                nameIconMap.put("img_cycling2", R.drawable.img_cycling2);
                nameIconMap.put("img_cycling4", R.drawable.img_cycling4);
                nameIconMap.put("img_buy1", R.drawable.img_buy1);
                nameIconMap.put("img_buy3", R.drawable.img_buy3);
                nameIconMap.put("img_buy4", R.drawable.img_buy4);
                nameIconMap.put("img_ticket1", R.drawable.img_ticket1);
                nameIconMap.put("img_ticket3", R.drawable.img_ticket3);
                nameIconMap.put("img_ticket4", R.drawable.img_ticket4);
                nameIconMap.put("img_delete1", R.drawable.img_delete1);
                nameIconMap.put("img_delete4", R.drawable.img_delete4);
                nameIconMap.put("img_pay_mobile4", R.drawable.img_pay_mobile4);
                nameIconMap.put("img_id_card1", R.drawable.img_id_card1);
                nameIconMap.put("img_id_card4", R.drawable.img_id_card4);


                nameIconMap.put("img_birthday1", R.drawable.img_birthday1);
                nameIconMap.put("img_birthday2", R.drawable.img_birthday2);
                nameIconMap.put("img_birthday3", R.drawable.img_birthday3);
                nameIconMap.put("img_birthday4", R.drawable.img_birthday4);
                nameIconMap.put("img_alarm1", R.drawable.img_alarm1);
                nameIconMap.put("img_alarm4", R.drawable.ic_alarm_notif);
                nameIconMap.put("img_alarm5", R.drawable.img_alarm5);
                nameIconMap.put("img_alarm6", R.drawable.img_alarm6);
                nameIconMap.put("img_meeting1", R.drawable.img_meeting1);
                nameIconMap.put("img_meeting2", R.drawable.img_meeting2);
                nameIconMap.put("img_meeting3", R.drawable.img_meeting3);
                nameIconMap.put("img_meeting4", R.drawable.img_meeting4);
                nameIconMap.put("img_lunch1", R.drawable.img_lunch1);
                nameIconMap.put("img_lunch2", R.drawable.img_lunch2);
                nameIconMap.put("img_lunch3", R.drawable.img_lunch3);
                nameIconMap.put("img_lunch4", R.drawable.img_lunch4);
                nameIconMap.put("img_lunch5", R.drawable.img_lunch5);
                nameIconMap.put("img_coffee1", R.drawable.img_coffee1);
                nameIconMap.put("img_coffee2", R.drawable.img_coffee2);
                nameIconMap.put("img_coffee3", R.drawable.img_coffee3);
                nameIconMap.put("img_coffee4", R.drawable.img_coffee4);
                nameIconMap.put("img_coffee5", R.drawable.img_coffee5);
                nameIconMap.put("img_milk_eggs1", R.drawable.img_milk_eggs1);
                nameIconMap.put("img_milk_eggs2", R.drawable.img_milk_eggs2);
                nameIconMap.put("img_milk_eggs3", R.drawable.img_milk_eggs3);
                nameIconMap.put("img_milk_eggs4", R.drawable.img_milk_eggs4);
                nameIconMap.put("img_credit_card1", R.drawable.img_credit_card1);
                nameIconMap.put("img_credit_card2", R.drawable.img_credit_card2);
                nameIconMap.put("img_credit_card3", R.drawable.img_credit_card3);
                nameIconMap.put("img_credit_card4", R.drawable.img_credit_card4);
                nameIconMap.put("img_credit_card5", R.drawable.img_credit_card5);
                nameIconMap.put("img_delivery1", R.drawable.img_delivery1);
                nameIconMap.put("img_delivery2", R.drawable.img_delivery2);
                nameIconMap.put("img_delivery3", R.drawable.img_delivery3);
                nameIconMap.put("img_delivery4", R.drawable.img_delivery4);
                nameIconMap.put("img_email1", R.drawable.img_email1);
                nameIconMap.put("img_email3", R.drawable.img_email3);
                nameIconMap.put("img_email4", R.drawable.ic_gmail_notif);
                nameIconMap.put("img_email5", R.drawable.img_email5);
                nameIconMap.put("img_reply1", R.drawable.img_reply1);
                nameIconMap.put("img_reply2", R.drawable.img_reply2);
                nameIconMap.put("img_reply4", R.drawable.img_reply4);
                nameIconMap.put("img_reply5", R.drawable.img_reply5);

                nameIconMap.put("img_leave1", R.drawable.img_leave1);
                nameIconMap.put("img_leave2", R.drawable.img_leave2);
                nameIconMap.put("img_leave3", R.drawable.img_leave3);
                nameIconMap.put("img_leave4", R.drawable.img_leave4);
                nameIconMap.put("img_visitor1", R.drawable.img_visitor1);
                nameIconMap.put("img_visitor2", R.drawable.img_visitor2);
                nameIconMap.put("img_visitor3", R.drawable.img_visitor3);
                nameIconMap.put("img_visitor4", R.drawable.img_visitor4);
                nameIconMap.put("img_presentation1", R.drawable.img_presentation1);
                nameIconMap.put("img_presentation2", R.drawable.img_presentation2);
                nameIconMap.put("img_presentation3", R.drawable.img_presentation3);
                nameIconMap.put("img_presentation4", R.drawable.img_presentation4);
                nameIconMap.put("img_doctor1", R.drawable.img_doctor1);
                nameIconMap.put("img_doctor2", R.drawable.img_doctor2);
                nameIconMap.put("img_doctor3", R.drawable.img_doctor3);
                nameIconMap.put("img_doctor4", R.drawable.img_doctor4);
                nameIconMap.put("img_exercise1", R.drawable.img_exercise1);
                nameIconMap.put("img_exercise2", R.drawable.img_exercise2);
                nameIconMap.put("img_exercise3", R.drawable.img_exercise3);
                nameIconMap.put("img_exercise4", R.drawable.img_exercise4);
                nameIconMap.put("img_standup1", R.drawable.img_standup1);
                nameIconMap.put("img_standup3", R.drawable.img_standup3);
                nameIconMap.put("img_standup4", R.drawable.img_standup4);
                nameIconMap.put("img_swimming1", R.drawable.img_swimming1);
                nameIconMap.put("img_swimming2", R.drawable.img_swimming2);
                nameIconMap.put("img_swimming3", R.drawable.img_swimming3);
                nameIconMap.put("img_swimming4", R.drawable.img_swimming4);
                nameIconMap.put("img_take_photo1", R.drawable.img_take_photo1);
                nameIconMap.put("img_take_photo2", R.drawable.img_take_photo2);
                nameIconMap.put("img_take_photo3", R.drawable.img_take_photo3);
                nameIconMap.put("img_take_photo4", R.drawable.img_take_photo4);
                nameIconMap.put("img_take_photo5", R.drawable.img_take_photo5);
                nameIconMap.put("img_sync_photos1", R.drawable.img_sync_photos1);
                nameIconMap.put("img_sync_photos2", R.drawable.img_sync_photos2);
                nameIconMap.put("img_sync_photos3", R.drawable.img_sync_photos3);
                nameIconMap.put("img_sync_photos4", R.drawable.img_sync_photos4);
                nameIconMap.put("img_download1", R.drawable.img_download1);
                nameIconMap.put("img_download2", R.drawable.img_download2);
                nameIconMap.put("img_download3", R.drawable.img_download3);
                nameIconMap.put("img_download4", R.drawable.img_download4);
                nameIconMap.put("img_download5", R.drawable.img_download5);

                nameIconMap.put("img_order_online1", R.drawable.img_order_online1);
                nameIconMap.put("img_order_online2", R.drawable.img_order_online2);
                nameIconMap.put("img_order_online3", R.drawable.img_order_online3);
                nameIconMap.put("img_order_online4", R.drawable.img_order_online4);
                nameIconMap.put("img_call1", R.drawable.img_call1);
                nameIconMap.put("img_call2", R.drawable.img_call2);
                nameIconMap.put("img_call3", R.drawable.img_call3);
                nameIconMap.put("img_call4", R.drawable.ic_call_notif);
                nameIconMap.put("img_call5", R.drawable.img_call5);
                nameIconMap.put("img_movie1", R.drawable.img_movie1);
                nameIconMap.put("img_movie2", R.drawable.img_movie2);
                nameIconMap.put("img_movie3", R.drawable.img_movie3);
                nameIconMap.put("img_movie4", R.drawable.img_movie4);
                nameIconMap.put("img_movie5", R.drawable.img_movie5);
                nameIconMap.put("img_valentine_day1", R.drawable.img_valentine_day1);
                nameIconMap.put("img_valentine_day2", R.drawable.img_valentine_day2);
                nameIconMap.put("img_valentine_day3", R.drawable.img_valentine_day3);
                nameIconMap.put("img_valentine_day4", R.drawable.img_valentine_day4);
                nameIconMap.put("img_mom_day1", R.drawable.img_mom_day1);
                nameIconMap.put("img_mom_day2", R.drawable.img_mom_day2);
                nameIconMap.put("img_mom_day3", R.drawable.img_mom_day3);
                nameIconMap.put("img_mom_day4", R.drawable.img_mom_day4);
                nameIconMap.put("img_battery_low1", R.drawable.img_battery_low1);
                nameIconMap.put("img_battery_low2", R.drawable.img_battery_low2);
                nameIconMap.put("img_battery_low3", R.drawable.img_battery_low3);
                nameIconMap.put("img_battery_low4", R.drawable.ic_battery_10_notif);
                nameIconMap.put("img_battery_low5", R.drawable.img_battery_low5);
                nameIconMap.put("img_car1", R.drawable.img_car1);
                nameIconMap.put("img_car2", R.drawable.img_car2);
                nameIconMap.put("img_car3", R.drawable.img_car3);
                nameIconMap.put("img_car4", R.drawable.img_car4);
                nameIconMap.put("img_bus1", R.drawable.img_bus1);
                nameIconMap.put("img_bus2", R.drawable.img_bus2);
                nameIconMap.put("img_bus3", R.drawable.img_bus3);
                nameIconMap.put("img_bus4", R.drawable.img_bus4);
                nameIconMap.put("img_flight1", R.drawable.img_flight1);
                nameIconMap.put("img_flight2", R.drawable.img_flight2);
                nameIconMap.put("img_flight3", R.drawable.img_flight3);
                nameIconMap.put("img_flight4", R.drawable.img_flight4);
                nameIconMap.put("img_flight5", R.drawable.img_flight5);
                nameIconMap.put("img_topup_cash1", R.drawable.img_topup_cash1);
                nameIconMap.put("img_topup_cash2", R.drawable.img_topup_cash2);
                nameIconMap.put("img_topup_cash3", R.drawable.img_topup_cash3);
                nameIconMap.put("img_topup_cash4", R.drawable.img_topup_cash4);

                nameIconMap.put("img_pay_rent1", R.drawable.img_pay_rent1);
                nameIconMap.put("img_pay_rent2", R.drawable.img_pay_rent2);
                nameIconMap.put("img_pay_rent3", R.drawable.img_pay_rent3);
                nameIconMap.put("img_pay_rent4", R.drawable.img_pay_rent4);
                nameIconMap.put("img_pay_cash1", R.drawable.img_pay_cash1);
                nameIconMap.put("img_pay_cash2", R.drawable.img_pay_cash2);
                nameIconMap.put("img_pay_cash3", R.drawable.img_pay_cash3);
                nameIconMap.put("img_pay_cash4", R.drawable.img_pay_cash4);
                nameIconMap.put("img_licence1", R.drawable.img_license1);
                nameIconMap.put("img_licence2", R.drawable.img_license2);
                nameIconMap.put("img_licence3", R.drawable.img_license3);
                nameIconMap.put("img_licence4", R.drawable.img_license4);
                nameIconMap.put("img_backup_computer1", R.drawable.img_backup_computer1);
                nameIconMap.put("img_backup_computer2", R.drawable.img_backup_computer2);
                nameIconMap.put("img_backup_computer3", R.drawable.img_backup_computer3);
                nameIconMap.put("img_backup_computer4", R.drawable.img_backup_computer4);

                nameIconMap.put("img_no_left_turn1", R.drawable.img_no_left_turn1);

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
