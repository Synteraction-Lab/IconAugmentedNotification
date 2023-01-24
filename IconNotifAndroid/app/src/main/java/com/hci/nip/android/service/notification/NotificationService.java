package com.hci.nip.android.service.notification;

import android.app.Notification;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.util.Log;

import androidx.core.app.NotificationCompat;

import com.hci.nip.android.MainActivity;
import com.hci.nip.android.actuators.DisplayActuator;
import com.hci.nip.android.actuators.NotificationActuator;
import com.hci.nip.android.actuators.model.NotificationData;
import com.hci.nip.android.util.FileUtil;

import org.slf4j.LoggerFactory;

import java.io.File;
import java.util.Timer;

import ch.qos.logback.classic.Logger;
import ch.qos.logback.classic.LoggerContext;
import ch.qos.logback.classic.android.LogcatAppender;
import ch.qos.logback.classic.encoder.PatternLayoutEncoder;
import ch.qos.logback.classic.spi.ILoggingEvent;
import ch.qos.logback.core.FileAppender;

public class NotificationService extends Service {
    private static final String TAG = NotificationService.class.getName();
    private static final String LOG_FILE_NAME = "nip.log";
    private static final org.slf4j.Logger LOGGER = LoggerFactory.getLogger(TAG);

    public static int FOREGROUND_SERVICE_ID = 468;

    public static final String ACTION_START_NOTIFICATION_SERVICE = "ACTION_START_NOTIFICATION_SERVICE";
    public static final String ACTION_STOP_NOTIFICATION_SERVICE = "ACTION_STOP_NOTIFICATION_SERVICE";
    public static final String ACTION_TEST_NOTIFICATION_SERVICE = "ACTION_TEST_NOTIFICATION_SERVICE";

    public static final String FILE_DIRECTORY = "notifications" + File.separator;
    private static final String DATA_DIRECTORY = FILE_DIRECTORY + "data";
    private static final String CONFIG_FILE = DATA_DIRECTORY + File.separator + "config.json";

    private NotificationActuator notificationActuator = null;
    private DisplayActuator displayActuator = null;

    private Timer timer = null;
    private boolean isServiceRunning = false;

    @Override
    public void onCreate() {
        super.onCreate();

        startServices();
    }

    @Override
    public void onDestroy() {
        Log.w(TAG, "onDestroy");
        super.onDestroy();

        releaseServices();
    }

    @Override
    public IBinder onBind(Intent intent) {
        // Used only in case of bound services.
        return null;
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        LOGGER.debug("[NotificationService] onStartCommand: action={}", (intent != null ? intent.getAction() : null));

        if (intent != null && intent.getAction() != null) {
            switch (intent.getAction()) {
                case ACTION_START_NOTIFICATION_SERVICE:
                    isServiceRunning = true;
                    startNotificationServiceOnForeground();
                    break;
                case ACTION_STOP_NOTIFICATION_SERVICE:
                    isServiceRunning = false;
                    stopNotificationServiceOnForeground();
                    break;
                case ACTION_TEST_NOTIFICATION_SERVICE:
                    displayTestNotification();
            }
        }

        return START_STICKY;
    }

    private void startNotificationServiceOnForeground() {
        LOGGER.debug("startNotificationServiceOnForeground");

        Intent notificationIntent = new Intent(this, MainActivity.class);
//        PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, notificationIntent, PendingIntent.FLAG_UPDATE_CURRENT);

        notificationIntent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
        PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, notificationIntent, 0);

        Notification notification = new NotificationCompat.Builder(this, NotificationActuator.CHANNEL_ID)
                .setContentTitle("Notification Service")
                .setContentText("Notifications")
                .setContentIntent(pendingIntent)
                .setAutoCancel(false)
                .setOngoing(true)
                .setVisibility(NotificationCompat.VISIBILITY_PUBLIC)
                .build();

        startForeground(FOREGROUND_SERVICE_ID, notification);
    }

    private void stopNotificationServiceOnForeground() {
        LOGGER.debug("stopNotificationServiceOnForeground");
        // Stop foreground service and remove the notification.
        stopForeground(true);
        // Stop the foreground service.
        stopSelf();
    }

    private void displayTestNotification() {
        if (!isServiceRunning) {
            notificationActuator.displayNotification(NotificationData.getToastNotification("Please click the 'START' button", 0));
//            stopSelf();
        } else {
            notificationActuator.displayNotification(getTestHeadsUpNotificationData());
        }
    }

    private int testMode = 0;

    private NotificationData getTestHeadsUpNotificationData() {
        NotificationData notificationData = NotificationData.getHeadsUpNotification("Test"
                , "This is a notification to test. Please adjust the volume of the smart glasses.");
        notificationData.setSmallIcon("#FFFFFF00 app");
        notificationData.setBigTextEnable(true);

        switch (testMode) {
            case 0:
                notificationData.setSoundEnable(false);
                notificationData.setVibrationEnable(false);
                break;
            case 1:
                notificationData.setSoundEnable(true);
                notificationData.setVibrationEnable(false);
                break;
            case 2:
                notificationData.setSoundEnable(false);
                notificationData.setVibrationEnable(true);
                break;
            default:
                notificationData.setSoundEnable(true);
                notificationData.setVibrationEnable(true);
        }


        Log.d(TAG, "Test notification mode :" + testMode);
        testMode++;
        testMode %= 4;

        return notificationData;
    }

    private void startServices() {
        configureLogbackDirectly();
        enableNotificationActuator();

        FileUtil.createDirectory(FileUtil.getAbsoluteFilePath(FILE_DIRECTORY));
    }

    private void releaseServices() {
        disableNotificationActuator();
    }

    private void enableNotificationActuator() {
        disableNotificationActuator();
        notificationActuator = new NotificationActuator(getApplicationContext(), "1");
        notificationActuator.activate();

        displayActuator = new DisplayActuator("2");
        displayActuator.activate();

    }

    private void disableNotificationActuator() {
        if (notificationActuator != null) {
            notificationActuator.deactivate();
        }
        notificationActuator = null;

        if (displayActuator != null) {
            displayActuator.deactivate();
        }
        displayActuator = null;
    }

    private void configureLogbackDirectly() {
        // reset the default context (which may already have been initialized)
        // since we want to reconfigure it
        LoggerContext lc = (LoggerContext) LoggerFactory.getILoggerFactory();
        lc.stop();

        // setup FileAppender
        PatternLayoutEncoder encoder1 = new PatternLayoutEncoder();
        encoder1.setContext(lc);
        encoder1.setPattern("%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n");
        encoder1.start();

        FileAppender<ILoggingEvent> fileAppender = new FileAppender<>();
        fileAppender.setContext(lc);
        fileAppender.setFile(FileUtil.getAbsoluteFilePath(LOG_FILE_NAME));
        fileAppender.setEncoder(encoder1);
        fileAppender.start();

        // setup LogcatAppender
        PatternLayoutEncoder encoder2 = new PatternLayoutEncoder();
        encoder2.setContext(lc);
        encoder2.setPattern("[%thread] %msg%n");
        encoder2.start();

        LogcatAppender logcatAppender = new LogcatAppender();
        logcatAppender.setContext(lc);
        logcatAppender.setEncoder(encoder2);
        logcatAppender.start();

        // add the newly created appenders to the root logger;
        // qualify Logger to disambiguate from org.slf4j.Logger
        Logger root = (Logger) LoggerFactory.getLogger(Logger.ROOT_LOGGER_NAME);
        root.addAppender(fileAppender);
        root.addAppender(logcatAppender);
    }

}
