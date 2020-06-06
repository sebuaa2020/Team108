package com.buaase.team108.wirelesstest;

import android.annotation.SuppressLint;
import android.os.Handler;
import android.os.Message;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class Manul extends AppCompatActivity {


    private Button buttonNewWayPoint;
    private Button buttonStart;
    private Button buttonFinish;
    private Button buttonrotateLeft;
    private Button buttonrotateRight;
    private Button buttonLeft;
    private Button buttonRight;
    private Button buttonUp;
    private Button buttonDown;
    private Button buttonGoto1;
    private Button buttonStop;

    public static Handler handler;

    @SuppressLint("HandlerLeak")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_manul);

        buttonStart = findViewById(R.id.startmap);
        buttonFinish = findViewById(R.id.finish);
        buttonrotateLeft = findViewById(R.id.leftrotate);
        buttonrotateRight = findViewById(R.id.rightrotate);
        buttonLeft = findViewById(R.id.left);
        buttonRight = findViewById(R.id.right);
        buttonUp = findViewById(R.id.forward);
        buttonDown = findViewById(R.id.backward);
        buttonNewWayPoint = findViewById(R.id.addNewWaypoint);
        buttonGoto1 = findViewById(R.id.buttonGoto1);
        buttonStop = findViewById(R.id.ButtonStop);

        handler = new Handler() {
            @Override
            public void handleMessage(Message msg) {
                switch (msg.what) {
                    case tcp.MESSAGE_RECEIVE:{
                        activeButton();
                        break;
                    }
                    case tcp.MESSAGE_SENDFAIL:{
                        activeButton();
                        Toast.makeText(Manul.this,"请重试",Toast.LENGTH_SHORT).show();
                        break;
                    }
                }
            }
        };

        buttonStart.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String str = "map_start";
                tcp.getinstance().handler.obtainMessage(tcp.MESSAGE_SEND, str).sendToTarget();
                disableButton();
            }
        });

        buttonFinish.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String str = "map_finish";
                tcp.getinstance().handler.obtainMessage(tcp.MESSAGE_SEND, str).sendToTarget();
                disableButton();
            }
        });

        buttonLeft.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String str = "move_left";
                tcp.getinstance().handler.obtainMessage(tcp.MESSAGE_SEND, str).sendToTarget();
                disableButton();
            }
        });

        buttonRight.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String str = "move_right";
                tcp.getinstance().handler.obtainMessage(tcp.MESSAGE_SEND, str).sendToTarget();
                disableButton();
            }
        });

        buttonUp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String str = "move_forward";
                tcp.getinstance().handler.obtainMessage(tcp.MESSAGE_SEND, str).sendToTarget();
                disableButton();
            }
        });

        buttonDown.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String str = "move_backward";
                tcp.getinstance().handler.obtainMessage(tcp.MESSAGE_SEND, str).sendToTarget();
                disableButton();
            }
        });

        buttonrotateLeft.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String str = "rotateleft";
                tcp.getinstance().handler.obtainMessage(tcp.MESSAGE_SEND, str).sendToTarget();
                disableButton();
            }
        });

        buttonrotateRight.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String str = "rotateright";
                tcp.getinstance().handler.obtainMessage(tcp.MESSAGE_SEND, str).sendToTarget();
                disableButton();
            }
        });

        buttonNewWayPoint.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String str = "grab";
                tcp.getinstance().handler.obtainMessage(tcp.MESSAGE_SEND, str).sendToTarget();
                disableButton();
            }
        });

        buttonGoto1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String str="navigation";
                tcp.getinstance().handler.obtainMessage(tcp.MESSAGE_SEND, str).sendToTarget();
                disableButton();
            }
        });

        buttonStop.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String str="stop";
                tcp.getinstance().handler.obtainMessage(tcp.MESSAGE_SEND, str).sendToTarget();
                disableButton();
            }
        });
    }

    private void activeButton(){
        buttonStart.setEnabled(true);
        buttonFinish.setEnabled(true);
        buttonUp.setEnabled(true);
        buttonDown.setEnabled(true);
        buttonLeft.setEnabled(true);
        buttonRight.setEnabled(true);
        buttonNewWayPoint.setEnabled(true);
        buttonGoto1.setEnabled(true);
        buttonrotateRight.setEnabled(true);
        buttonrotateLeft.setEnabled(true);
        buttonStop.setEnabled(true);
    }

    private void disableButton(){
        buttonStart.setEnabled(false);
        buttonFinish.setEnabled(false);
        buttonUp.setEnabled(false);
        buttonDown.setEnabled(false);
        buttonLeft.setEnabled(false);
        buttonRight.setEnabled(false);
        buttonNewWayPoint.setEnabled(false);
        buttonGoto1.setEnabled(false);
        buttonrotateRight.setEnabled(false);
        buttonrotateLeft.setEnabled(false);
        buttonStop.setEnabled(false);
    }


}
