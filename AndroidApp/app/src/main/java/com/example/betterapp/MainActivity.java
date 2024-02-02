package com.example.betterapp;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import android.annotation.SuppressLint;
import android.app.Application;
import android.content.Context;
import android.net.http.HttpException;
import android.net.http.UrlRequest;
import android.net.http.UrlResponseInfo;
import android.nfc.Tag;
import android.os.Build;
import android.os.Bundle;
import android.os.ext.SdkExtensions;
import android.text.Layout;
import android.util.DisplayMetrics;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.google.common.io.CharStreams;

import org.chromium.net.CronetEngine;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.net.HttpURLConnection;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.DataOutputStream;
import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.SSLPeerUnverifiedException;

import java.net.URL;
import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.security.cert.Certificate;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Future;

public class MainActivity extends AppCompatActivity
    implements View.OnClickListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        DisplayMetrics displayMetrics = new DisplayMetrics();
        getWindowManager().getDefaultDisplay().getMetrics(displayMetrics);
        float displayHeight = displayMetrics.heightPixels;
        int displayWidth = displayMetrics.widthPixels;

        TextView titleText = findViewById(R.id.titleText);
        titleText.setTextSize(displayHeight * 0.02f);

        TextView equationLabelText = findViewById(R.id.equationInputLabel);
        equationLabelText.setTextSize((int) (displayHeight * 0.01));
        equationLabelText.setHeight((int) (displayHeight * 0.05));
        ConstraintLayout.LayoutParams labelTextParams = (ConstraintLayout.LayoutParams) equationLabelText.getLayoutParams();
        labelTextParams.topMargin = (int) (displayHeight * 0.03);
        equationLabelText.setLayoutParams(labelTextParams);


        EditText equationInputField = findViewById(R.id.userEquationInputField);
        equationInputField.setWidth(displayWidth/2);
        equationInputField.setHeight((int) (displayHeight * 0.05));
        ConstraintLayout.LayoutParams textFieldParams = (ConstraintLayout.LayoutParams) equationInputField.getLayoutParams();
        textFieldParams.setMarginStart((int) (displayWidth * 0.02));
        textFieldParams.topMargin = (int) (displayHeight * 0.03);
        equationInputField.setLayoutParams(textFieldParams);

        TextView x_valueLabelText = findViewById(R.id.user_x_valueInputLabel);
        x_valueLabelText.setTextSize((int) (displayHeight * 0.01));
        x_valueLabelText.setHeight((int) (displayHeight * 0.05));
        ConstraintLayout.LayoutParams x_valueLabelParams = (ConstraintLayout.LayoutParams) x_valueLabelText.getLayoutParams();
        x_valueLabelParams.topMargin = (int) (displayHeight * 0.03);
        x_valueLabelText.setLayoutParams(x_valueLabelParams);

        EditText x_valueInputField = findViewById(R.id.user_x_valueInputField);
        x_valueInputField.setWidth(displayWidth/2);
        x_valueInputField.setHeight((int) (displayHeight * 0.05));
        ConstraintLayout.LayoutParams x_valueInputParams = (ConstraintLayout.LayoutParams) x_valueInputField.getLayoutParams();
        x_valueInputParams.setMarginStart((int) (displayWidth * 0.02));
        x_valueInputParams.topMargin = (int) (displayHeight * 0.03);
        x_valueInputField.setLayoutParams(x_valueInputParams);

        Button inputConfirmButton = findViewById(R.id.inputConfirmButton);
        inputConfirmButton.setWidth(displayWidth/3);
        inputConfirmButton.setHeight((int) (displayHeight/15));
        inputConfirmButton.setTextSize(displayHeight * 0.01f);
        ConstraintLayout.LayoutParams inputConfirmButtonParams = (ConstraintLayout.LayoutParams) inputConfirmButton.getLayoutParams();
        inputConfirmButtonParams.topMargin = (int) (displayHeight * 0.03);
        inputConfirmButton.setLayoutParams(inputConfirmButtonParams);
        inputConfirmButton.setOnClickListener(this);


        TextView resultHeader = findViewById(R.id.resultHeader);
        resultHeader.setTextSize(displayHeight * 0.01f);
        ConstraintLayout.LayoutParams resultHeaderParams = (ConstraintLayout.LayoutParams) resultHeader.getLayoutParams();
        resultHeaderParams.topMargin = (int) (displayHeight * 0.05f);
        resultHeader.setLayoutParams(resultHeaderParams);

        TextView resultText = findViewById(R.id.resultText);
        resultText.setTextSize(displayHeight * 0.008f);
        resultText.setHeight((int) (displayHeight * 0.3));

        Button faxButton = findViewById(R.id.faxButton);
        faxButton.setTextSize(displayHeight * 0.01f);
        faxButton.setOnClickListener(this);
    }


    /*   Test user input processing
    public String possibleInput(String input) {
        switch (input.toLowerCase()) {
            case "krishna":
                return "Absolute AI maniac!";
            case "brennan":
                return "Breeno the Cheerio head (Ed Sheeran?!)";
            case "aryan":
                return "Get back to work!!! enthusiast";
            case "nikson":
                return "Goofy goober";
            default:
                return "additional functionalities yet to be added...";
        }
    }

         */

    @SuppressLint("NonConstantResourceId")
    @Override
    public void onClick(View v) {
        if (v.getId() == R.id.faxButton) {
            Toast.makeText(this, R.string.toast_text, Toast.LENGTH_SHORT).show();
        } else if (v.getId() == R.id.inputConfirmButton) {
            EditText textField = findViewById(R.id.inputField);
            EditText x_Field = findViewById(R.id.user_x_valueInputField);
            String expression = textField.getText().toString();
            String x_value = x_Field.toString();
            TextView resultText = findViewById(R.id.resultText);

            //resultText.setText(possibleInput(textField.getText().toString()));
        }
    }

    /*  How the data should be sent to the server...
    {
        "equation": "x^2",
        "x": "5"
    }
    */

}