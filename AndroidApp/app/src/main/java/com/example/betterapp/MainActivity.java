package com.example.betterapp;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Rect;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.fragment.app.Fragment;
import androidx.navigation.NavBackStackEntry;
import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.NavigationUI;

import com.bumptech.glide.Glide;
import com.bumptech.glide.load.engine.DiskCacheStrategy;
import com.bumptech.glide.request.RequestOptions;
import com.caverock.androidsvg.SVG;
import com.caverock.androidsvg.SVGParseException;
import com.example.betterapp.databinding.ActivityMainBinding;
import com.google.android.material.bottomnavigation.BottomNavigationView;
import com.google.android.material.navigation.NavigationBarView;

public class MainActivity extends AppCompatActivity {
    private static final String TAG = "MainActivity";
    //private final CompositeDisposable disposables = new CompositeDisposable();
    //TextView resultText; // Global variable so it can be accessed by multiple methods
    //MutableLiveData<String> resultLiveData = new MutableLiveData<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ActivityMainBinding binding = ActivityMainBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        // get application window height
        Rect screenRect = getWindow().getWindowManager().getCurrentWindowMetrics().getBounds();
        float screenHeight = screenRect.height();
        int screenWidth = screenRect.width();
        // width not required as it will just be match_parent

        // set background gif
        ImageView background = findViewById(R.id.backgroundImageView);
        Glide.with(this)
                .asGif()
                .load(R.drawable.auto_diff_background_gif)
                .diskCacheStrategy(DiskCacheStrategy.ALL)
                .into(background);

        // set main banner
        ImageView banner = findViewById(R.id.banner);
        try {
            // load SVG resource
            SVG bannerSVG = SVG.getFromResource(this, R.raw.banner);
            // convert to BitMap
            Bitmap bitmap = Bitmap.createBitmap((int) bannerSVG.getDocumentWidth(), (int) bannerSVG.getDocumentHeight(), Bitmap.Config.ARGB_8888);
            Canvas canvas = new Canvas(bitmap);
            bannerSVG.renderToCanvas(canvas);

            ViewGroup.LayoutParams bannerLayoutParams = banner.getLayoutParams();
            bannerLayoutParams.width = screenWidth;
            bannerLayoutParams.height = (int) (screenHeight * 0.10);

            if (bannerLayoutParams instanceof ViewGroup.MarginLayoutParams) {
                ViewGroup.MarginLayoutParams bannerMarginLayoutParams = (ViewGroup.MarginLayoutParams) bannerLayoutParams;
                bannerMarginLayoutParams.topMargin = 0;
            }

            banner.setLayoutParams(bannerLayoutParams);

            Glide.with(this)
                    .load(bitmap)
                    .apply(RequestOptions.centerCropTransform())
                    .into(banner);

        } catch (SVGParseException e) {
            throw new RuntimeException(e);
        }



        // set navigation bar
        BottomNavigationView navView = binding.getRoot().findViewById(R.id.nav_view);
        NavController navController = Navigation.findNavController(this, R.id.nav_host_fragment_activity_main);
        NavigationUI.setupWithNavController(navView, navController);

        View navFragment = findViewById(R.id.nav_host_fragment_activity_main);
        //setNavFragment(screenHeight, navFragment);
        setNavBar(screenHeight, navView);
    }

    public static void setNavFragment(float windowHeight, View navFragmentView) {
        if (navFragmentView != null) {
            ViewGroup.LayoutParams navFragmentLayoutParams = navFragmentView.getLayoutParams();
            navFragmentLayoutParams.height = (int) (windowHeight * 0.85);
            navFragmentView.setLayoutParams(navFragmentLayoutParams);
        }
    }

    public static void setNavBar(float windowHeight, BottomNavigationView navBar) {
        ViewGroup.LayoutParams navBarLayoutParams = navBar.getLayoutParams();
        navBarLayoutParams.height = (int) (windowHeight * 0.10);
        navBar.setLayoutParams(navBarLayoutParams);
    }
    
    @Override
    protected void onDestroy() {
        super.onDestroy();
        // disposables.clear(); // avoids memory leaks
    }
}
