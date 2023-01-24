package com.hci.nip.android.service.notification;

import android.app.Service;

import com.hci.nip.android.repository.DataRepository;
import com.hci.nip.android.service.BroadcastService;
import com.hci.nip.android.service.ServiceProvider;

public abstract class NotificationServiceProvider extends Service {

    protected BroadcastService broadcastService;
    protected DataRepository dataRepository;

    private final InnerServiceProvider innerServiceProvider;

    public NotificationServiceProvider() {
        innerServiceProvider = new InnerServiceProvider();
        broadcastService = innerServiceProvider.getBroadcastService();
        dataRepository = innerServiceProvider.getDataRepository();
    }

    private final class InnerServiceProvider extends ServiceProvider{

        private BroadcastService getBroadcastService(){
            return broadcastService;
        }

        private DataRepository getDataRepository(){
            return dataRepository;
        }
    }
}


