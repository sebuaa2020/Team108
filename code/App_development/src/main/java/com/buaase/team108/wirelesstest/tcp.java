package com.buaase.team108.wirelesstest;

import android.annotation.SuppressLint;
import android.content.Context;
import android.icu.text.SymbolTable;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.os.Trace;
import android.util.Log;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketException;

import static android.content.Context.WIFI_SERVICE;


public class tcp extends Thread{
    public static final int MESSAGE_TCPREADY = 0;
    public static final int MESSAGE_SEND = 1;
    public static final int MESSAGE_RECEIVE = 2;
    public static final int MESSAGE_TCPCLOSE = 3;
    public static final int MESSAGE_SENDFAIL = 4;
    private static final String linuxip = "192.168.1.103";
    private static final String winip = "192.168.1.104";

    private static tcp instance;
    public Handler handler;
    private boolean rcvFlag;
    private boolean rcvGoing;

    public tcp(){}

    public static tcp getinstance(){
        if(instance==null){
            instance = new tcp();

            instance.start();
        }
        return instance;
    }

    public void startServerReplyListener(final BufferedReader reader) {
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    String response;
                    while ((response = reader.readLine()) != null) {
                        Log.d("Test",response);
                        if(response.contains("follow")){
                            Follow.handler.obtainMessage(MESSAGE_RECEIVE,response).sendToTarget();
                        }else{
                            Manul.handler.obtainMessage(MESSAGE_RECEIVE,response).sendToTarget();
                        }
                        rcvFlag=true;
                    }

                } catch (IOException e) {
                    e.printStackTrace();
                }
                rcvGoing=false;
            }
        }).start();
    }

    private boolean connectSend(String str){
        BufferedReader reader = null;
        BufferedWriter writer = null;
        Socket socket = new Socket();
        try {
            socket.connect( new InetSocketAddress( linuxip, 9999), 500);
        } catch (Exception e) {
            Log.d("Test","connection fail!");
        }
        if(!socket.isConnected()){
            return false;
        }
        try {
            socket.setTcpNoDelay(true);
            reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            writer = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
        } catch (IOException e) {
            e.printStackTrace();
        }
        rcvGoing=true;
        startServerReplyListener(reader);
        try {
            Log.d("Test","send "+str);
            writer.write(str);
            writer.flush();
//            reader.close();
//            writer.close();
//            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return true;
    }

    @SuppressLint("HandlerLeak")
    @Override
    public void run() {
        Looper.prepare();
        handler = new Handler(){
            public void handleMessage (Message msg) {
                switch (msg.what){
                    case(MESSAGE_SEND):
                        Log.d("Test","run, receive msg, type MESSAGE_SEND");
                        int counter=5;
                        rcvFlag=false;
                        while(counter>0 && !rcvFlag){
                            if(!connectSend((String)msg.obj)) {
                                counter--;
                                continue;
                            }
                            while(rcvGoing){
                                try {
                                    Thread.sleep(100);
                                } catch (InterruptedException e) {
                                    e.printStackTrace();
                                }
                            }
                            counter--;
                        }
                        if(!rcvFlag){
                            Log.d("Test","run, send Fail");
                            if(((String) msg.obj).contains("follow")){
                                Follow.handler.obtainMessage(MESSAGE_SENDFAIL).sendToTarget();
                            }else{
                                Manul.handler.obtainMessage(MESSAGE_SENDFAIL).sendToTarget();
                            }
                        }
                }
            }
        };
        Looper.loop();
    }
}
