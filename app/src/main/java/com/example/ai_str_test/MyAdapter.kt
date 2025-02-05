package com.example.ai_str_test

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.LinearLayout
import android.widget.TextView
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class MyAdapter(private val dataList: List<String>) : RecyclerView.Adapter<MyAdapter.MyViewHolder>() {

    class MyViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val textView: TextView = itemView.findViewById(R.id.textView)
        val rv: RecyclerView = itemView.findViewById(R.id.child_rv)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.item_layout, parent, false)
        return MyViewHolder(view)
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        holder.textView.text = dataList[position]
        holder.rv.layoutManager = LinearLayoutManager(holder.rv.context, RecyclerView.HORIZONTAL, false)
        val dataList = arrayListOf<String>()

        for (i in 1..20) {
            dataList.add("Child Item $i")
        }

        val adapter = MyChildAdapter(dataList)
        holder.rv.adapter = adapter
    }

    override fun getItemCount(): Int {
        return dataList.size
    }
}
