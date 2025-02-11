package com.example.ai_str_test

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.airbnb.lottie.LottieAnimationView


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
//        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
      //  setContentView(R.layout.lottie)
       // lottie()

        val recyclerView : RecyclerView = findViewById(R.id.recyclerView)
        recyclerView.layoutManager = LinearLayoutManager(this)
        val dataList = arrayListOf<String>()

        for (i in 1..20) {
            dataList.add("Widget TitleHIIIII $i")

        }

        val adapter = MyAdapter(dataList)

        recyclerView.adapter = adapter


    }


    private fun lottie() {
        val lottie = findViewById<LottieAnimationView>(R.id.animationView)
        lottie.setAnimationFromUrl("https://webappsstatic.paytm.com/growth/assets/home/snow.lottie")
        lottie.playAnimation()

    }



}

