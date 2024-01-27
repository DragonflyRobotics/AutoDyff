package com.example.betterapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import android.annotation.SuppressLint;
import android.nfc.Tag;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

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

        TextView labelText = findViewById(R.id.inputLabel);
        labelText.setTextSize((int) (displayHeight * 0.01));
        labelText.setHeight((int) (displayHeight * 0.05));
        ConstraintLayout.LayoutParams labelTextParams = (ConstraintLayout.LayoutParams) labelText.getLayoutParams();
        labelTextParams.topMargin = (int) (displayHeight * 0.03);
        labelText.setLayoutParams(labelTextParams);


        EditText textField = findViewById(R.id.inputField);
        textField.setWidth(displayWidth/2);
        textField.setHeight((int) (displayHeight * 0.05));
        ConstraintLayout.LayoutParams textFieldParams = (ConstraintLayout.LayoutParams) textField.getLayoutParams();
        textFieldParams.setMarginStart((int) (displayWidth * 0.02));
        textFieldParams.topMargin = (int) (displayHeight * 0.03);
        textField.setLayoutParams(textFieldParams);

        Button inputConfirmButton = findViewById(R.id.inputConfirmButton);
        inputConfirmButton.setWidth((int) (displayWidth/3));
        inputConfirmButton.setHeight((int) (displayHeight/15));
        inputConfirmButton.setTextSize(displayHeight * 0.01f);
        ConstraintLayout.LayoutParams inputConfirmButtonParams = (ConstraintLayout.LayoutParams) inputConfirmButton.getLayoutParams();
        inputConfirmButtonParams.topMargin = (int) (displayHeight * 0.03f);
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

    @SuppressLint("NonConstantResourceId")
    @Override
    public void onClick(View v) {
        if (v.getId() == R.id.faxButton) {
            Toast.makeText(this, R.string.toast_text, Toast.LENGTH_SHORT).show();
        } else if (v.getId() == R.id.inputConfirmButton) {
            EditText textField = findViewById(R.id.inputField);
            TextView resultText = findViewById(R.id.resultText);

            resultText.setText(possibleInput(textField.getText().toString()));
        }
    }
}