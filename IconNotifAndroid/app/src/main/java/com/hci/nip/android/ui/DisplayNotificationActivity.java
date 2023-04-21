package com.hci.nip.android.ui;

import android.content.Context;
import android.content.Intent;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Path;
import android.graphics.Point;
import android.graphics.drawable.Drawable;
import android.media.AudioManager;
import android.media.ToneGenerator;
import android.os.Bundle;
import android.util.Log;
import android.view.KeyEvent;
import android.view.View;
import android.view.ViewGroup;
import android.view.animation.TranslateAnimation;
import android.widget.ImageView;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;

import androidx.core.graphics.drawable.DrawableCompat;

import com.hci.nip.android.BaseActivity;
import com.hci.nip.android.IntentActionType;
import com.hci.nip.android.actuators.HapticActuator;
import com.hci.nip.android.actuators.NotificationActuator;
import com.hci.nip.android.actuators.model.HapticData;
import com.hci.nip.android.actuators.model.NotificationData;
import com.hci.nip.android.sensors.model.TouchBarEventType;
import com.hci.nip.android.service.BroadcastService;
import com.hci.nip.android.service.notification.NotificationService;
import com.hci.nip.android.util.FileUtil;
import com.hci.nip.android.util.KeyEventUtil;
import com.hci.nip.base.actuator.Actuator;
import com.hci.nip.base.actuator.ActuatorType;
import com.hci.nip.base.actuator.model.DisplayData;
import com.hci.nip.base.util.DeviceManagerUtil;
import com.hci.nip.glass.R;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

/**
 * TODO: change these activities to fragments & view model (ref: https://developer.android.com/guide/components/fragments.html#java)
 */
public class DisplayNotificationActivity extends BaseActivity {

    private static final String TAG = DisplayNotificationActivity.class.getName();
    private static final String CONFIG_INTERNAL_DELIMITER = ",";

    private ViewGroup layoutMain;
    private ViewGroup layoutNotification;
    private ViewGroup layoutCue;
    private ViewGroup layoutMcq;

    private TextView textViewHeading;
    private TextView textViewSubHeading;
    private TextView textViewSubHeading2;
    private TextView textViewContent;
    private ImageView iconImage;
    private ImageView iconImage2;

    private TextView textViewTitle;
    private TextView textViewAppName;
    private TextView textViewMessage;
    private ImageView iconSmall;
    private ImageView iconLarge;

    private TextView textViewMcqQuestion;
    private RadioGroup radioGroupMcqChoices;
    private RadioButton radioButtonMcqChoice1;
    private RadioButton radioButtonMcqChoice2;
    private RadioButton radioButtonMcqChoice3;
    private RadioButton radioButtonMcqChoice4;

    private ScheduledExecutorService scheduledExecutorService;

    private final List<IntentActionType> intentActionTypes = Arrays.asList(
            IntentActionType.DISPLAY_UPDATE,
            IntentActionType.NOTIFICATION_UPDATE
    );

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_display_notification_epson);

        initializeUIElements();
    }

    @Override
    protected void onPause() {
        super.onPause();
        Log.e(TAG, "onPause");

        stopExecutorService();
        tempCueModalityData = null;
    }

    @Override
    protected void onResume() {
        super.onResume();
        Log.e(TAG, "onResume");

        startExecutorService();
    }

    private void startExecutorService() {
        stopExecutorService();
        scheduledExecutorService = Executors.newScheduledThreadPool(2);
    }

    private void stopExecutorService() {
        if (scheduledExecutorService != null) {
            scheduledExecutorService.shutdownNow();
        }
        scheduledExecutorService = null;
    }

    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);
        if (hasFocus) {
            hideSystemUI();
        }
    }

    private void hideSystemUI() {
        // ref: https://developer.android.com/training/system-ui/immersive#java
        View decorView = getWindow().getDecorView();
        decorView.setSystemUiVisibility(
                View.SYSTEM_UI_FLAG_IMMERSIVE
                        // Set the content to appear under the system bars so that the
                        // content doesn't resize when the system bars hide and show.
                        | View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                        | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                        | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                        // Hide the nav bar and status bar
                        | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                        | View.SYSTEM_UI_FLAG_FULLSCREEN
                        // keep screen on
                        | View.KEEP_SCREEN_ON
        );
    }

    private void showSystemUI() {
        View decorView = getWindow().getDecorView();
        decorView.setSystemUiVisibility(
                View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                        | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                        | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN);
    }


    @Override
    public void onIntentReceive(Context context, IntentActionType intentActionType, Intent intent) {
        Log.d(TAG, "[DISPLAY] onIntentReceive");
        switch (intentActionType) {
            case DISPLAY_UPDATE:
                updateUI(intent);
                break;
            case NOTIFICATION_UPDATE:
                updateNotificationUI(intent);
                break;
        }
    }

    private long lastClickedMillis = 0;

    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        TouchBarEventType type = KeyEventUtil.getTouchBarEventType(keyCode);

        if (System.currentTimeMillis() - lastClickedMillis > 100) {
            lastClickedMillis = System.currentTimeMillis();

            if (TouchBarEventType.ONE_FINGER_SWIPE_FORWARD == type || TouchBarEventType.ONE_FINGER_SWIPE_BACKWARD == type) {
                touchBarSwiped();
            }
        }
        return super.onKeyDown(keyCode, event);
    }


    private void touchBarSwiped() {
        Log.d(TAG, "screenClicked");

        if (tempCueModalityData != null) {
            handleCueModalityData();
        } else {
            clearNotification(1);
        }

    }

    private void handleCueModalityData() {
        CueModalityData cueModalityData = tempCueModalityData;
        cueModalityData.startMillis = lastClickedMillis;

        scheduledExecutorService.submit(() -> updateDisplay(cueModalityData.displayData));
        scheduledExecutorService.submit(() -> writeCueModalityResult(cueModalityData, "OPEN"));

        clearNotification(cueModalityData.durationMillis);

        tempCueModalityData = null;
    }

    private void clearNotification(long millis) {
        scheduledExecutorService.schedule(() -> {
                    deactivateNotificationDisplay();
                    deactivateMcqDisplay();
                    deactivateMainDisplay();
                }
                , millis, TimeUnit.MILLISECONDS);
    }

    @Override
    public List<IntentActionType> getIntentActionTypes() {
        return intentActionTypes;
    }

    private void initializeUIElements() {
        layoutMain = findViewById(R.id.displayMainLayout);

        textViewHeading = findViewById(R.id.displayProfileHeading);
        textViewSubHeading = findViewById(R.id.displayProfileSubheading);
        textViewSubHeading2 = findViewById(R.id.displayProfileSubheading2);
        textViewContent = findViewById(R.id.displayProfileContent);
        iconImage = findViewById(R.id.displayImage);
        iconImage2 = findViewById(R.id.displayImage2);

        layoutNotification = findViewById(R.id.layoutNotification);

        textViewAppName = findViewById(R.id.displayAppName);
        iconSmall = findViewById(R.id.displayAppIcon);

        textViewTitle = findViewById(R.id.displayTitle);
        iconLarge = findViewById(R.id.displayLargeIcon);
        textViewMessage = findViewById(R.id.displayMessage);

        textViewHeading.setText(null);
        textViewSubHeading.setText(null);
        textViewSubHeading2.setText(null);
        textViewContent.setText(null);
        iconImage.setImageResource(0);
        iconImage2.setImageResource(0);

        textViewAppName.setText(null);
        iconSmall.setImageResource(0);

        textViewTitle.setText(null);
        textViewMessage.setText(null);
        iconLarge.setImageResource(0);

        layoutCue = findViewById(R.id.layoutCue);

        initializeMcqLayout();
    }

    private void initializeMcqLayout() {
        layoutMcq = findViewById(R.id.layoutMcq);

        textViewMcqQuestion = findViewById(R.id.mcqQuestion);
        radioGroupMcqChoices = findViewById(R.id.mcqRadioGroup);
        radioButtonMcqChoice1 = findViewById(R.id.mcqChoice1);
        radioButtonMcqChoice2 = findViewById(R.id.mcqChoice2);
        radioButtonMcqChoice3 = findViewById(R.id.mcqChoice3);
        radioButtonMcqChoice4 = findViewById(R.id.mcqChoice4);

//        radioButtonMcqChoice1.setOnFocusChangeListener((focused, hasFocus) -> {
//            if (hasFocus) {
//                radioButtonMcqChoice1.setChecked(true);
//            }
//        });
//        radioButtonMcqChoice2.setOnFocusChangeListener((focused, hasFocus) -> {
//            if (hasFocus) {
//                radioButtonMcqChoice2.setChecked(true);
//            }
//        });
//        radioButtonMcqChoice3.setOnFocusChangeListener((focused, hasFocus) -> {
//            if (hasFocus) {
//                radioButtonMcqChoice3.setChecked(true);
//            }
//        });
//        radioButtonMcqChoice4.setOnFocusChangeListener((focused, hasFocus) -> {
//            if (hasFocus) {
//                radioButtonMcqChoice4.setChecked(true);
//            }
//        });
    }

    private void updateUI(Intent intent) {
        Log.v(TAG, "[DISPLAY] Updating UI");
        long intentId = BroadcastService.getBroadcastIntentId(intent);
        // get request from dataRepository
        DisplayData displayData = (DisplayData) dataRepository.getRequest(intentId);
        // process it
        updateUIElements(displayData);
        //send the response (for this we wil directly send the same request as response)
        dataRepository.addResponse(intentId, displayData);
    }

    private void updateNotificationUI(Intent intent) {
        Log.v(TAG, "[DISPLAY] Updating Notification UI");
        long intentId = BroadcastService.getBroadcastIntentId(intent);
        NotificationData notificationData = (NotificationData) dataRepository.getRequest(intentId);
        updateNotificationUIElements(notificationData);
    }

    private void updateUIElements(DisplayData displayData) {
        String config = displayData.getConfig();
        if (config == null || config.isEmpty()) {
            startExecutorService();
            updateDisplay(displayData);
        } else {
            updateConfigDisplay(displayData);
        }
    }

    private void updateNotificationUIElements(NotificationData notificationData) {
        String config = notificationData.getConfig();
        if (config == null || config.isEmpty()) {
            startExecutorService();
            updateNotification(notificationData);
        } else {
            updateConfigNotification(notificationData);
        }
    }

    private void activateMainDisplay() {
        Log.d(TAG, "activateMainDisplay");
        runOnUiThread(() -> {
            layoutMcq.setVisibility(View.GONE);
            layoutMain.setVisibility(View.VISIBLE);
        });
    }

    private void deactivateMainDisplay() {
        Log.d(TAG, "deactivateMainDisplay");
        runOnUiThread(() -> {
            layoutMain.setVisibility(View.GONE);
        });
    }

    private void clearMainDisplay() {
        Log.d(TAG, "clearMainDisplay");
        runOnUiThread(() -> {
            textViewHeading.setText(null);
            textViewSubHeading.setText(null);
            textViewSubHeading2.setText(null);
            textViewContent.setText(null);
            iconImage.setImageResource(0);
            iconImage2.setImageResource(0);
        });
    }

    private void activateNotificationDisplay() {
        Log.d(TAG, "activateNotificationDisplay");
        runOnUiThread(() -> {
            layoutNotification.setVisibility(View.VISIBLE);
        });
    }

    private void deactivateNotificationDisplay() {
        Log.d(TAG, "deactivateNotificationDisplay");
        runOnUiThread(() -> {
            layoutNotification.setVisibility(View.GONE);
        });
        clearNotificationDisplay();
    }

    private void clearNotificationDisplay() {
        Log.d(TAG, "deactivateNotificationDisplay");
        runOnUiThread(() -> {
            textViewAppName.setText(null);
            iconSmall.setImageResource(0);
            textViewTitle.setText(null);
            textViewMessage.setText(null);
            iconLarge.setImageResource(0);
            // TODO: may need to remove this
            changeBackground(layoutNotification, 4);
        });
    }

    private void transparentNotificationDisplay() {
        Log.d(TAG, "deactivateNotificationDisplay");
        runOnUiThread(() -> {
            textViewAppName.setAlpha(0);
            iconSmall.setAlpha(0f);
            textViewTitle.setAlpha(0);
            textViewMessage.setAlpha(0);
            iconLarge.setAlpha(0f);
            changeBackground(layoutNotification, 16);
        });
    }


    private void activateMcqDisplay() {
        Log.d(TAG, "activateMcQDisplay");
        runOnUiThread(() -> {
            layoutMcq.setVisibility(View.VISIBLE);
        });
    }

    private void clearMcqDisplay() {
        Log.d(TAG, "clearMcQDisplay");
        runOnUiThread(() -> {
            radioButtonMcqChoice1.setChecked(false);
            radioButtonMcqChoice2.setChecked(false);
            radioButtonMcqChoice2.setChecked(false);
            radioButtonMcqChoice4.setChecked(false);
            radioGroupMcqChoices.clearCheck();
        });
    }

    private void deactivateMcqDisplay() {
        Log.d(TAG, "deactivateMcqDisplay");
        runOnUiThread(() -> {
            layoutMcq.setVisibility(View.GONE);
        });
    }

    private void activateCueDisplay() {
        Log.d(TAG, "activateCueDisplay");
        runOnUiThread(() -> {
            layoutCue.setVisibility(View.VISIBLE);
        });
    }

    private void deactivateCueDisplay() {
        Log.d(TAG, "deactivateCueDisplay");
        runOnUiThread(() -> {
            layoutCue.removeAllViews();
            layoutCue.setVisibility(View.GONE);
        });
    }

    private void updateDisplay(DisplayData displayData) {
        Log.d(TAG, "updateDisplay: " + displayData);

        deactivateCueDisplay();
        deactivateNotificationDisplay();
        updateDisplayElements(displayData, 1);
        activateMainDisplay();
    }

    private void updateDisplayElements(DisplayData displayData, float alpha) {
        NotificationActuator.ColorText heading = NotificationActuator.getColorText(displayData.getHeading());
        NotificationActuator.ColorText subHeading = NotificationActuator.getColorText(displayData.getSubheading());
        NotificationActuator.ColorText subHeading2 = NotificationActuator.getColorText(displayData.getContent());
        NotificationActuator.ColorText content = NotificationActuator.getColorText(displayData.getContent());
        NotificationActuator.ColorText image = NotificationActuator.getColorText(displayData.getImage());
        NotificationActuator.ColorText image2 = NotificationActuator.getColorText(displayData.getAudio());

        runOnUiThread(() -> {
            changeTextView(textViewHeading, heading, alpha);
            changeTextView(textViewSubHeading, subHeading, alpha);
            changeTextView(textViewSubHeading2, subHeading2, alpha);
//            changeTextView(textViewContent, content, alpha);
            changeImageView(iconImage, image, alpha);
            changeImageView(iconImage2, image2, alpha);
        });
    }

    private void updateNotification(NotificationData notificationData) {
        Log.d(TAG, "updateNotification: " + notificationData);

        if (notificationData.isVibrationEnable()) {
            scheduledExecutorService.submit(this::provideHapticFeedback);
        }
        if (notificationData.isSoundEnable()) {
            scheduledExecutorService.submit(this::provideAuditoryFeedback);
        }

        deactivateCueDisplay();
        deactivateMcqDisplay();
        updateNotificationElements(notificationData, 1);
        activateNotificationDisplay();
    }

    private void updateNotificationElements(NotificationData notificationData, float alpha) {
        NotificationActuator.ColorText title = NotificationActuator.getColorText(notificationData.getTitle());
        NotificationActuator.ColorText content = NotificationActuator.getColorText(notificationData.getMessage());
        NotificationActuator.ColorText image = NotificationActuator.getColorText(notificationData.getLargeIcon());
        NotificationActuator.ColorText appName = NotificationActuator.getColorText(notificationData.getAppName());
        NotificationActuator.ColorText appIcon = NotificationActuator.getColorText(notificationData.getSmallIcon());

        runOnUiThread(() -> {
            changeTextView(textViewAppName, appName, alpha);
            changeImageView(iconSmall, appIcon, alpha);
            changeTextView(textViewTitle, title, alpha);
            changeTextView(textViewMessage, content, alpha);
            changeImageView(iconLarge, image, alpha);
            changeBackground(layoutNotification, Math.min((int) (alpha * 255) + 16, 255));
        });
    }

    private void updateNotificationElementsIndividually(NotificationData notificationData, float alpha, float alphaIcon, float alphaTitle, float alphaMessage) {
        NotificationActuator.ColorText title = NotificationActuator.getColorText(notificationData.getTitle());
        NotificationActuator.ColorText content = NotificationActuator.getColorText(notificationData.getMessage());
        NotificationActuator.ColorText image = NotificationActuator.getColorText(notificationData.getLargeIcon());
        NotificationActuator.ColorText appName = NotificationActuator.getColorText(notificationData.getAppName());
        NotificationActuator.ColorText appIcon = NotificationActuator.getColorText(notificationData.getSmallIcon());

        runOnUiThread(() -> {
            changeTextView(textViewAppName, appName, alphaIcon);
            changeImageView(iconSmall, appIcon, alphaIcon);
            changeTextView(textViewTitle, title, alphaTitle);
            changeTextView(textViewMessage, content, alphaMessage);
            changeImageView(iconLarge, image, alpha);
            changeBackground(layoutNotification, Math.min((int) (alpha * 255) + 16, 255));
        });
    }

    private void changeTextView(TextView textView, NotificationActuator.ColorText colorText, float alpha) {
        textView.setText(colorText.getText());
        if (colorText.getColor() != 0 && colorText.getText() != null) {
            textView.setTextColor(colorText.getColor());
        }
        if (textView.getAlpha() != alpha) {
            textView.setAlpha(alpha);
        }
    }

    private void changeImageView(ImageView imageView, NotificationActuator.ColorText colorText, float alpha) {
        Log.d(TAG, "changeImageView: " + colorText);
        imageView.setImageResource(NotificationActuator.NotificationIconMapping.getIcon(colorText.getText()));
        if (colorText.getColor() != 0) {
            imageView.setColorFilter(colorText.getColor());
        }
        if (imageView.getAlpha() != alpha) {
            imageView.setAlpha(alpha);
        }
    }

    private void changeBackground(ViewGroup layout, int alpha) {
        Drawable background = layout.getBackground();
        if (background.getAlpha() != alpha) {
            background.setAlpha(alpha);
        }
    }

    private static NotificationData transformDisplayToNotification(DisplayData displayData) {
        NotificationData notificationData = NotificationData.getCustomNotification(displayData.getHeading(), displayData.getContent());
        notificationData.setLargeIcon(displayData.getImage());
        notificationData.setConfig(displayData.getConfig());
        return notificationData;
    }


    private void updateConfigDisplay(DisplayData displayData) {
        Log.d(TAG, "updateConfigDisplay: " + displayData);
        String[] configContents = getConfigContents(displayData.getConfig());

        String configType = configContents[0];

        if (!configType.contains("NO_REFRESH")) {
            startExecutorService();
        }

        if (isCueModalityConfig(configType)) {
            DisplayData originalNotification = new DisplayData(displayData);
            originalNotification.setConfig(null);

            List<CueModalityData> cueModalityDataList = getCueDataList(configContents, originalNotification);
            updateCueModalityData(cueModalityDataList);
        } else if (isShapeConfig(configType)) {
            List<ShapeData> shapeDataList = getShapeDataList(configContents);
            updateShapeData(shapeDataList);
        } else if ("MCQ_CHOICES".equals(configType)) {
            updateMcqData(displayData);
        } else if ("NO_REFRESH".equals(configType)) {
            updateDisplayWithoutRefresh(displayData);
        } else {
            Log.e(TAG, "Unrecognized config type: " + configType);
        }
    }

    private void updateConfigNotification(NotificationData notificationData) {
        Log.d(TAG, "updateConfigNotification: " + notificationData);
        String[] configContents = getConfigContents(notificationData.getConfig());
        String configType = configContents[0];

        deactivateCueDisplay();
        deactivateMcqDisplay();

        if (!configType.contains("NO_REFRESH")) {
            startExecutorService();

            clearMainDisplay();
            clearNotificationDisplay();
            activateNotificationDisplay();
        }

        if ("PROGRESSIVE".equals(configType)) {
            processConfigNotificationProgressive(notificationData, configContents);
        } else if ("PROGRESSIVE_WITH_DISPLAY".equals(configType)) {
            processConfigNotificationProgressiveDisplay(notificationData, configContents);
        } else if ("PROGRESSIVE_WITH_NO_REFRESH".equals(configType)) {
            // FORMAT: PROGRESSIVE_WITH_NO_REFRESH, <slide_appear_millis>, <slide_disappear_millis>, <appear_intensity_millis>, <disappear_intensity_millis>,
            processProgressiveNotificationOnly(notificationData, configContents);
        } else if ("PROGRESSIVE_WITH_DISPLAY_TIMING".equals(configType)) {
            processConfigNotificationProgressiveDisplayTiming(notificationData, configContents);
        } else if (configType.startsWith("PROGRESSIVE_WITH_DISPLAY_CUE")) {
            processConfigNotificationProgressiveDisplayCue(notificationData, configContents);
        } else if (configType.startsWith("PROGRESSIVE_WITH_NO_REFRESH_CUE")) {
            processConfigNotificationProgressiveNoRefreshCue(notificationData, configContents);
        } else {
            Log.e(TAG, "Unrecognized config: " + configType);
        }
    }

    private void processConfigNotificationProgressiveDisplayCue(NotificationData notificationData, String[] configContents) {
        // FORMAT: PROGRESSIVE_WITH_DISPLAY_CUE_<DISPLAY_TIME>, <slide_appear_millis>, <slide_disappear_millis>,
        // <appear_intensity_millis>, <disappear_intensity_millis>,
        // <heading>, <sub_heading>, <content>

        processProgressiveNotificationDisplayCueOnly(notificationData, configContents[0]);
        // show notification after cue
        processConfigNotificationProgressiveDisplay(notificationData, configContents);
    }

    private void processConfigNotificationProgressiveNoRefreshCue(NotificationData notificationData, String[] configContents) {
        // FORMAT: PROGRESSIVE_WITH_NO_REFRESH_CUE_<DISPLAY_TIME>, <slide_appear_millis>, <slide_disappear_millis>,
        // <appear_intensity_millis>, <disappear_intensity_millis>,

        processProgressiveNotificationDisplayCueOnly(notificationData, configContents[0]);
        // show notification after cue
        processProgressiveNotificationOnly(notificationData, configContents);
    }

    private void processProgressiveNotificationDisplayCueOnly(NotificationData notificationData, String configType) {
        // cue start position = (1280 - 480) / 2
        final String cueConfig = "LINE_HORIZONTAL,480,#FFFFFF,5,5,";

        long cueDisplayTime = getProgressiveDisplayCueTimeFromConfig(configType);
        long when = notificationData.getWhen();

        // show cue
        scheduledExecutorService.schedule(() -> {
            List<ShapeData> shapeDataList = getShapeDataList(getConfigContents(cueConfig));
            updateShapeData(shapeDataList);
        }, when - cueDisplayTime, TimeUnit.MILLISECONDS);

        // remove cue
        scheduledExecutorService.schedule(() -> {
            deactivateCueDisplay();
            activateNotificationDisplay();
        }, when - 30, TimeUnit.MILLISECONDS);
    }

    private static long getProgressiveDisplayCueTimeFromConfig(String configType) {
        // FORMAT: PROGRESSIVE_WITH_DISPLAY_CUE_<DISPLAY_TIME> or PROGRESSIVE_WITH_NO_REFRESH_CUE_<DISPLAY_TIME>
        String[] configElements = configType.split("_");
        String configTime = configElements[configElements.length - 1];
        try {
            return Long.parseLong(configTime);
        } catch (NumberFormatException e) {
            Log.e(TAG, "Error in parsing cue time: " + configType);
            return 2000; // default value
        }
    }

    private void processConfigNotificationProgressiveDisplayTiming(NotificationData notificationData, String[] configContents) {
        // FORMAT: PROGRESSIVE_WITH_DISPLAY_TIMING, <slide_appear_millis>, <slide_disappear_millis>,
        // <appear_intensity_millis:icon>, <appear_intensity_millis:title>, <appear_intensity_millis:message>,
        // <disappear_intensity_millis>,
        // <heading>, <sub_heading>, <content>

        transparentNotificationDisplay();
        processDisplayDataInNotificationConfig(configContents, 7);
        processProgressiveNotificationOnlyIndividually(notificationData, configContents);
    }

    private void processProgressiveNotificationOnlyIndividually(NotificationData notificationData, String[] configContents) {
        long when = notificationData.getWhen();
        long dwellTime = notificationData.getDuration();

        int slideAppearMillis = Integer.parseInt(configContents[1]);
        int slideDisappearMillis = Integer.parseInt(configContents[2]);
        int appearToFullIntensityMillisIcon = Integer.parseInt(configContents[3]);
        int appearToFullIntensityMillisTitle = Integer.parseInt(configContents[4]);
        int appearToFullIntensityMillisMessage = Integer.parseInt(configContents[5]);
        int disappearToZeroIntensityMillis = Integer.parseInt(configContents[6]);

        final int stepGap = 100;
        long startAppearingTime = when + 1;

        // start of animation = appearing time / 8
        int appearToFullIntensityMillis = Collections.max(Arrays.asList(appearToFullIntensityMillisIcon, appearToFullIntensityMillisTitle, appearToFullIntensityMillisMessage));

//            slideNotificationDown(startAppearingTime + appearToFullIntensityMillis / 8, slideAppearMillis);
        slideNotificationDown(startAppearingTime + stepGap, slideAppearMillis);
        changeNotificationAppearanceIndividually(notificationData, startAppearingTime, 0, 1f, stepGap, appearToFullIntensityMillis / stepGap,
                appearToFullIntensityMillisIcon / stepGap, appearToFullIntensityMillisTitle / stepGap, appearToFullIntensityMillisMessage / stepGap);
        long startDisappearingTime = startAppearingTime + stepGap + appearToFullIntensityMillis + dwellTime;
        changeNotificationAppearance(notificationData, startDisappearingTime, 1f, 0, stepGap, disappearToZeroIntensityMillis / stepGap);
        slideNotificationUp(startDisappearingTime + disappearToZeroIntensityMillis - stepGap - slideDisappearMillis, slideDisappearMillis);
//            slideNotificationUp(startDisappearingTime + disappearToZeroIntensityMillis * 7 / 8 - slideDisappearMillis, slideDisappearMillis);
    }

    private void processConfigNotificationProgressiveDisplay(NotificationData notificationData, String[] configContents) {
        // FORMAT: PROGRESSIVE_WITH_DISPLAY, <slide_appear_millis>, <slide_disappear_millis>, <appear_intensity_millis>, <disappear_intensity_millis>, <heading>, <sub_heading>, <content>

        transparentNotificationDisplay();
        processDisplayDataInNotificationConfig(configContents, 5);
        processProgressiveNotificationOnly(notificationData, configContents);
    }

    private void processDisplayDataInNotificationConfig(String[] configContents, int start_index) {
        // start_index = index of <heading>
        // FORMAT: PROGRESSIVE_WITH_DISPLAY, <slide_appear_millis>, <slide_disappear_millis>, <appear_intensity_millis>, <disappear_intensity_millis>, <heading>, <sub_heading>, <content>
        DisplayData displayData = new DisplayData(
                fixString(configContents[start_index]),
                fixString(configContents[start_index + 1]),
                fixString(configContents[start_index + 2])
        );
        updateDisplayElements(displayData, 1);
        activateMainDisplay();
    }

    private void processProgressiveNotificationOnly(NotificationData notificationData, String[] configContents) {
        // FORMAT: PROGRESSIVE_WITH_XXX, <slide_appear_millis>, <slide_disappear_millis>, <appear_intensity_millis>, <disappear_intensity_millis>,
        long when = notificationData.getWhen();
        long dwellTime = notificationData.getDuration();

        int slideAppearMillis = Integer.parseInt(configContents[1]);
        int slideDisappearMillis = Integer.parseInt(configContents[2]);
        int appearToFullIntensityMillis = Integer.parseInt(configContents[3]);
        int disappearToZeroIntensityMillis = Integer.parseInt(configContents[4]);

        final int stepGap = 100;
        long startAppearingTime = when + 1;

        // start of animation = appearing time / 8
//            slideNotificationDown(startAppearingTime + appearToFullIntensityMillis / 8, slideAppearMillis);
        slideNotificationDown(startAppearingTime + stepGap, slideAppearMillis);
        changeNotificationAppearance(notificationData, startAppearingTime, 0, 1f, stepGap, appearToFullIntensityMillis / stepGap);
        long startDisappearingTime = startAppearingTime + stepGap + appearToFullIntensityMillis + dwellTime;
        changeNotificationAppearance(notificationData, startDisappearingTime, 1f, 0, stepGap, disappearToZeroIntensityMillis / stepGap);
        slideNotificationUp(startDisappearingTime + disappearToZeroIntensityMillis - stepGap - slideDisappearMillis, slideDisappearMillis);
//            slideNotificationUp(startDisappearingTime + disappearToZeroIntensityMillis * 7 / 8 - slideDisappearMillis, slideDisappearMillis);
    }

    private void processConfigNotificationProgressive(NotificationData notificationData, String[] configContents) {
        // FORMAT: PROGRESSIVE, <start_alpha = 0>, <end_alpha = 1>, <step_count>, <step_gap_millis>
        float startAlpha = Integer.parseInt(configContents[1]);
        float endAlpha = Integer.parseInt(configContents[2]);
        int stepCount = Integer.parseInt(configContents[3]);
        int stepGap = Integer.parseInt(configContents[4]);

        long when = notificationData.getWhen();
        changeNotificationAppearance(notificationData, when, startAlpha, endAlpha, stepGap, stepCount);
    }

    private String fixString(String data) {
        if (data == null || data.isEmpty()) {
            return data;
        }
        return data.replace("|", ",");
    }

    private void changeNotificationAppearance(NotificationData notificationData, long when, float startAlpha, float endAlpha, int stepGap, int stepCount) {
        float alphaIncrement = (endAlpha - startAlpha) / stepCount;
        for (int i = 1; i <= stepCount; i++) {
            float newAlpha = startAlpha + i * alphaIncrement;
            scheduledExecutorService.schedule(() -> {
                updateNotificationElements(notificationData, newAlpha);
            }, when + i * stepGap, TimeUnit.MILLISECONDS);
        }
    }

    private void changeNotificationAppearanceIndividually(NotificationData notificationData, long when, float startAlpha, float endAlpha, int stepGap,
                                                          int stepCountMax, int stepCountIcon, int stepCountTitle, int stepCountMessage) {
        float alphaDifference = endAlpha - startAlpha;
        float alphaIncrement = alphaDifference / stepCountMax;
        float alphaIncrementIcon = alphaDifference / stepCountIcon;
        float alphaIncrementTitle = alphaDifference / stepCountTitle;
        float alphaIncrementMessage = alphaDifference / stepCountMessage;
        for (int i = 1; i <= stepCountMax; i++) {
            float newAlpha = startAlpha + i * alphaIncrement;
            float newAlphaIcon = startAlpha + i * alphaIncrementIcon;
            float newAlphaTitle = startAlpha + i * alphaIncrementTitle;
            float newAlphaMessage = startAlpha + i * alphaIncrementMessage;
            scheduledExecutorService.schedule(() -> {
                updateNotificationElementsIndividually(notificationData, getSupportedAlpha(newAlpha),
                        getSupportedAlpha(newAlphaIcon), getSupportedAlpha(newAlphaTitle), getSupportedAlpha(newAlphaMessage));
            }, when + i * stepGap, TimeUnit.MILLISECONDS);
        }
    }

    private static float getSupportedAlpha(float alpha) {
        if (alpha <= 0) {
            return 0;
        } else if (alpha >= 1) {
            return 1;
        } else {
            return alpha;
        }
    }

    private void slideNotificationDown(long when, long duration) {
        scheduledExecutorService.schedule(() -> slide(layoutNotification, -layoutNotification.getHeight(), 0, duration), when, TimeUnit.MILLISECONDS);
    }

    private void slideNotificationUp(long when, long duration) {
        scheduledExecutorService.schedule(() -> slide(layoutNotification, 0, -layoutNotification.getHeight(), duration), when, TimeUnit.MILLISECONDS);
    }

    private void slide(View view, int startY, int endY, long duration) {
//        view.setVisibility(View.VISIBLE);
        TranslateAnimation animate = new TranslateAnimation(0,
                0,
                startY,
                endY);
        animate.setDuration(duration);
        animate.setFillAfter(true);
        runOnUiThread(() -> view.startAnimation(animate));
    }


    private String[] getConfigContents(String config) {
        String trimmedGlossData = config.trim();

        String[] configContents = trimmedGlossData.split(CONFIG_INTERNAL_DELIMITER, -1);
        for (int i = 0; i < configContents.length; i++) {
            configContents[i] = configContents[i].trim();
        }
        Log.d(TAG, configContents.length + " : " + Arrays.toString(configContents));
        return configContents;
    }

    private static boolean isShapeConfig(String configValue) {
        for (Shape shape : Shape.values()) {
            if (shape.name().equalsIgnoreCase(configValue))
                return true;
        }
        return false;
    }

    private static boolean isCueModalityConfig(String configValue) {
        for (CueModalityType cueModalityType : CueModalityType.values()) {
            if (cueModalityType.name().equalsIgnoreCase(configValue))
                return true;
        }
        return false;
    }

    private static List<ShapeData> getShapeDataList(String[] configContents) {
        // ShapeData FORMAT: <shape> , <radius>, <color>, <x>, <y>, <extra>

        final int MAX_ELEMENTS = 6;
        List<ShapeData> shapeDataList = new ArrayList<>(configContents.length / MAX_ELEMENTS);

        for (int i = 0; i < configContents.length / MAX_ELEMENTS; i++) {
            ShapeData shapeData = new ShapeData(
                    Shape.valueOf(configContents[i * MAX_ELEMENTS]),
                    Integer.parseInt(configContents[i * MAX_ELEMENTS + 1]),
                    Color.parseColor(configContents[i * MAX_ELEMENTS + 2])
            );
            shapeData.x = Integer.parseInt(configContents[i * MAX_ELEMENTS + 3]);
            shapeData.y = Integer.parseInt(configContents[i * MAX_ELEMENTS + 4]);
            shapeData.extra = configContents[i * MAX_ELEMENTS + 5];

            shapeDataList.add(shapeData);
        }
        return shapeDataList;
    }

    private List<CueModalityData> getCueDataList(String[] configContents, DisplayData displayData) {
        // Cue FORMAT: <cue_type>, <unique_id>, <display_duration>, <reward>
        final int MAX_ELEMENTS = 4;

        List<CueModalityData> cueModalityDataList = new ArrayList<>(configContents.length / MAX_ELEMENTS);

        for (int i = 0; i < configContents.length / MAX_ELEMENTS; i++) {
            CueModalityData cueModalityData = new CueModalityData(
                    CueModalityType.valueOf(configContents[i * MAX_ELEMENTS]),
                    configContents[i * MAX_ELEMENTS + 1],
                    displayData
            );

            cueModalityData.durationMillis = Integer.parseInt(configContents[i * MAX_ELEMENTS + 2]);
            cueModalityData.reward = Integer.parseInt(configContents[i * MAX_ELEMENTS + 3]);

            cueModalityDataList.add(cueModalityData);
        }
        return cueModalityDataList;
    }

    private CueModalityData tempCueModalityData = null;

    private void updateCueModalityData(List<CueModalityData> cueModalityDataList) {
        deactivateNotificationDisplay();
        activateCueDisplay();

        for (CueModalityData cueModalityData : cueModalityDataList) {
            cueModalityData.startMillis = System.currentTimeMillis();

            tempCueModalityData = cueModalityData;

            switch (cueModalityData.cueModalityType) {
                case VISUAL:
                    scheduledExecutorService.submit(this::displayVisualModalityCue);
                    break;
                case AUDITORY:
                    scheduledExecutorService.submit(this::provideAuditoryFeedback);
                    break;
                case HAPTIC:
                    scheduledExecutorService.submit(this::provideHapticFeedback);
                    break;
            }
            scheduledExecutorService.schedule(this::deactivateCueDisplay, cueModalityData.durationMillis, TimeUnit.MILLISECONDS);

            scheduledExecutorService.submit(() -> writeCueModalityResult(cueModalityData, "SHOW"));
        }
    }

    private void displayVisualModalityCue() {
        Log.d(TAG, "displayVisualModalityCue");
        ShapeData visualCue = new ShapeData(Shape.CIRCLE, 20, Color.RED);
        visualCue.x = 240;
        visualCue.y = 20;
        updateShapeData(Collections.singletonList(visualCue));
    }

    private void provideAuditoryFeedback() {
        Log.d(TAG, "showAuditoryFeedback");
        ToneGenerator toneGen1 = new ToneGenerator(AudioManager.STREAM_NOTIFICATION, 60);
        toneGen1.startTone(ToneGenerator.TONE_DTMF_0, 500);
    }

    private void provideHapticFeedback() {
        Log.d(TAG, "displayHapticModalityCue");
        getHapticActuator().vibrate(Collections.singletonList(new HapticData(1, 500, 500)));
    }

    private HapticActuator getHapticActuator() {
        List<Actuator> actuatorList = DeviceManagerUtil.getFilteredActuatorsByType(deviceManager.getActuators(), ActuatorType.ACTUATOR_TYPE_VIBRATOR);
        HapticActuator actuator = (HapticActuator) actuatorList.get(0);
        actuator.activate();
        return actuator;
    }

    private void writeCueModalityResult(CueModalityData cueModalityData, String status) {
        Log.d(TAG, "writeCueModalityResult: " + status + ", " + cueModalityData);

        final String file = NotificationService.FILE_DIRECTORY + "cue_modality_result.csv";
        String result = cueModalityData.id + "," + cueModalityData.cueModalityType + "," + cueModalityData.reward + "," + cueModalityData.startMillis + "," + status + "\n";
        try {
            FileUtil.appendFile(result.getBytes(), file);
        } catch (FileUtil.FileException e) {
            Log.e(TAG, "Error in writing", e);
        }
    }

    private void updateShapeData(List<ShapeData> shapeDataList) {
        deactivateNotificationDisplay();
        activateCueDisplay();

        runOnUiThread(() -> {
            for (ShapeData shapeData : shapeDataList) {
                Log.d(TAG, "Update shape: " + shapeData);
                CueView child = new CueView(getContext(), shapeData);
                layoutCue.addView(child);
                child.invalidate();
            }
        });
    }

    private void updateMcqData(DisplayData displayData) {
        Log.d(TAG, "updateMcqData");
        deactivateNotificationDisplay();
        deactivateCueDisplay();
        deactivateMainDisplay();

        String question = displayData.getHeading();
        // FORMAT: MCQ_CHOICES
        // <choice_1>|<choice_2>|<choice_3>|<choice_4>|selected
        String[] options = displayData.getContent().trim().split("\\|", -1);

        String selectedChoiceString = options[4];
//        Log.d(TAG, "MCQ options: " + Arrays.toString(options));
        int selectedChoice = selectedChoiceString.trim().isEmpty() ? -1 : Integer.parseInt(selectedChoiceString);

        updateMcqElements(question, options, selectedChoice);
        activateMcqDisplay();
    }

    private void updateMcqElements(String question, String[] options, int selected) {
        Log.d(TAG, "selected: " + selected);
        runOnUiThread(() -> {

            textViewMcqQuestion.setText(question);
            radioButtonMcqChoice1.setText(options[0]);
            radioButtonMcqChoice2.setText(options[1]);
            radioButtonMcqChoice3.setText(options[2]);
            radioButtonMcqChoice4.setText(options[3]);

            radioButtonMcqChoice1.setChecked(false);
            radioButtonMcqChoice2.setChecked(false);
            radioButtonMcqChoice3.setChecked(false);
            radioButtonMcqChoice3.setChecked(false);
            radioGroupMcqChoices.clearCheck();

            switch (selected) {
                case 1:
                    radioButtonMcqChoice1.setChecked(true);
                    break;
                case 2:
                    radioButtonMcqChoice2.setChecked(true);
                    break;
                case 3:
                    radioButtonMcqChoice3.setChecked(true);
                    break;
                case 4:
                    radioButtonMcqChoice4.setChecked(true);
                    break;
            }
        });
    }

    private void updateDisplayWithoutRefresh(DisplayData displayData) {
        Log.d(TAG, "updateDisplayWithoutRefresh");

        DisplayData newDisplayData = new DisplayData(displayData);
        newDisplayData.setHeading(fixString(displayData.getHeading()));
        newDisplayData.setSubheading(fixString(displayData.getSubheading()));
        newDisplayData.setContent(fixString(displayData.getContent()));

        updateDisplayElements(newDisplayData, 1);
    }

    private static class CueView extends View {

        private Paint paint = null;
        private ShapeData shapeData = null;

        public CueView(Context context, ShapeData shapeData) {
            super(context);

            this.paint = new Paint();
            this.shapeData = shapeData;
        }

        @Override
        protected void onDraw(Canvas canvas) {
            super.onDraw(canvas);

            Log.d(TAG, "Shape: " + shapeData);

            int radius = shapeData.radius;
            int color = shapeData.color;
            int x = shapeData.x;
            int y = shapeData.y;
            String extra = shapeData.extra;

            paint.setColor(color);

            int halfRadius = radius / 2;

            switch (shapeData.shape) {
                case CIRCLE:
                    paint.setStyle(Paint.Style.FILL);
                    canvas.drawCircle(x, y, radius, paint);
                    break;
                case SQUARE:
                    paint.setStyle(Paint.Style.FILL);
                    canvas.drawRect(x - halfRadius, y - halfRadius, x + halfRadius, y + halfRadius, paint);
                    break;
                case TRIANGLE:
                    paint.setStyle(Paint.Style.FILL);
                    drawTriangle(canvas, paint, x - halfRadius, y + halfRadius, radius, radius, false);
                    break;
                case RHOMBUS:
                    paint.setStyle(Paint.Style.FILL);
                    drawRhombus(canvas, paint, x, y, radius);
                    break;
                case CROSS:
                    paint.setStyle(Paint.Style.FILL);
                    drawCross(canvas, paint, x, y, radius);
                    break;
                case ICON:
                    Drawable d = DrawableCompat.wrap(getResources().getDrawable(NotificationActuator.NotificationIconMapping.getIcon(extra), null));
                    d.setBounds(x - halfRadius, y - halfRadius, x + halfRadius, y + halfRadius);
                    DrawableCompat.setTint(d, color);
                    d.draw(canvas);
                    break;
                case LINE_HORIZONTAL:
                    paint.setStyle(Paint.Style.FILL);
                    paint.setStrokeWidth(2);
                    canvas.drawLine(x, y, x + radius, y, paint);
                    break;
                case TEXT:
                    // see https://stackoverflow.com/questions/2655402/android-canvas-drawtext
                    int textSizePixel = radius;
                    paint.setTextSize(textSizePixel);
                    canvas.drawText(extra, x, y + textSizePixel, paint);
                    break;
            }
        }

        // ref: https://kylewbanks.com/blog/drawing-triangles-rhombuses-and-other-shapes-on-android-canvas,
        // ref: https://medium.com/better-programming/learn-all-android-canvas-draw-functions-dd5d6595884a
        private void drawTriangle(Canvas canvas, Paint paint, int x, int y, int width, int height, boolean inverted) {
            Point p1 = new Point(x, y);
            int pointX = x + width / 2;
            int pointY = inverted ? y + height : y - height;

            Point p2 = new Point(pointX, pointY);
            Point p3 = new Point(x + width, y);

            Path path = new Path();
            path.setFillType(Path.FillType.EVEN_ODD);
            path.moveTo(p1.x, p1.y);
            path.lineTo(p2.x, p2.y);
            path.lineTo(p3.x, p3.y);
            path.close();

            canvas.drawPath(path, paint);
        }

        private void drawRhombus(Canvas canvas, Paint paint, int x, int y, int width) {
            int halfWidth = width / 2;

            Path path = new Path();
            path.moveTo(x, y + halfWidth); // Top
            path.lineTo(x - halfWidth, y); // Left
            path.lineTo(x, y - halfWidth); // Bottom
            path.lineTo(x + halfWidth, y); // Right
            path.lineTo(x, y + halfWidth); // Back to Top
            path.close();

            canvas.drawPath(path, paint);
        }

        private void drawCross(Canvas canvas, Paint paint, int x, int y, int width) {
            int oneSixthWidth = width / 6 + 1;
            int halfWidth = width / 2;

            canvas.drawRect(x - oneSixthWidth, y - halfWidth, x + oneSixthWidth, y + halfWidth, paint);
            canvas.drawRect(x - halfWidth, y - oneSixthWidth, x + halfWidth, y + oneSixthWidth, paint);
        }

    }

    private static class ShapeData {
        Shape shape;
        int radius;
        int color;
        int x = 0;
        int y = 0;
        String extra;

        public ShapeData(Shape shape, int radius, int color) {
            this.shape = shape;
            this.radius = radius;
            this.color = color;
        }

        @Override
        public String toString() {
            return "ShapeData{" +
                    "shape=" + shape +
                    ", radius=" + radius +
                    ", color=" + color +
                    ", x=" + x +
                    ", y=" + y +
                    ", extra=" + extra +
                    '}';
        }

    }

    private enum Shape {
        CIRCLE("CIRCLE"),
        SQUARE("SQUARE"),
        TRIANGLE("TRIANGLE"),
        RHOMBUS("RHOMBUS"),
        CROSS("CROSS"),
        ICON("ICON"),
        TEXT("TEXT"),
        LINE_HORIZONTAL("LINE_HORIZONTAL"),
        ;

        private String value;

        Shape(String value) {
            this.value = value;
        }

    }

    private static class CueModalityData {
        CueModalityType cueModalityType;
        String id;
        DisplayData displayData;
        int durationMillis = 15000;
        int reward = 1;

        long startMillis = 0;

        public CueModalityData(CueModalityType cue, String id, DisplayData displayData) {
            this.cueModalityType = cue;
            this.id = id;
            this.displayData = displayData;
        }

        @Override
        public String toString() {
            return "CueModalityData{" +
                    "cueModalityType=" + cueModalityType +
                    ", id='" + id + '\'' +
                    ", displayData=" + displayData +
                    ", duration=" + durationMillis +
                    ", reward=" + reward +
                    '}';
        }
    }

    private enum CueModalityType {
        VISUAL("VISUAL"),
        AUDITORY("AUDITORY"),
        HAPTIC("HAPTIC"),
        ;

        private String value;

        CueModalityType(String value) {
            this.value = value;
        }
    }

}
