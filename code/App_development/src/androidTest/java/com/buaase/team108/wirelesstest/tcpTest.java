package com.buaase.team108.wirelesstest;

import org.junit.Test;

import static org.junit.Assert.*;

public class tcpTest {

    @Test
    public void getinstanceTest1() {
        tcp testTcp1=tcp.getinstance();
    }


    @Test
    public void getinstanceTest2() {
        tcp testTcp1=tcp.getinstance();
        tcp testTcp2=tcp.getinstance();
        tcp testTcp3=tcp.getinstance();
        tcp testTcp4=tcp.getinstance();
        tcp testTcp5=tcp.getinstance();
        tcp testTcp6=tcp.getinstance();
    }


    @Test
    public void startServerReplyListenerTest() {
        tcp testTcp1=tcp.getinstance();
    }


    @Test
    public void run() {
    }
}