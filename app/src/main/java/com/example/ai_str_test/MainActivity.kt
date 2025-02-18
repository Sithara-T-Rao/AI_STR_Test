package com.example.ai_str_test

import MasterView
import android.content.Context
import android.os.Bundle
import android.util.Log
import androidx.activity.ComponentActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.airbnb.lottie.LottieAnimationView
import com.example.ai_str_test.Helper.loadJsonFromAssets
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
//        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
      //  setContentView(R.layout.lottie)
       // lottie()

        val recyclerView : RecyclerView = findViewById(R.id.recyclerView)
        recyclerView.layoutManager = LinearLayoutManager(this)
       /* val dataList = arrayListOf<String>()

        for (i in 1..20) {
            dataList.add("Widget TitleHIIIII $i")

        }*/
        val dataList = parseJson()
        val adapter = MyAdapter(dataList)

        recyclerView.adapter = adapter


    }

    fun parseJson(): List<MasterView> {
        val jsonString = loadJsonFromAssets(this, "master_data.json")
        jsonString?.let {
            val gson = Gson()
            val type = object : TypeToken<List<MasterView>>() {}.type
            val masterList: List<MasterView> = gson.fromJson(it, type)


//            for (view in masterList) {
//                Log.d("JSON", "Title: ${view.view.title}")
//                for (item in view.view.items) {
//                    Log.d("JSON", "Item Name: ${item.name}, Type: ${item.type}")
//                }
//            }

            return masterList
        }
        return arrayListOf()
    }


    private fun lottie() {
        val lottie = findViewById<LottieAnimationView>(R.id.animationView)
        lottie.setAnimationFromUrl("https://webappsstatic.paytm.com/growth/assets/home/snow.lottie")
        lottie.playAnimation()

    }



}

