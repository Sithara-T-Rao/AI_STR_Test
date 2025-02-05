package com.example.ai_str_test

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class MyChildAdapter(private val dataList: List<String>) : RecyclerView.Adapter<MyChildAdapter.MyChildViewHolder>() {

    class MyChildViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val textView: TextView = itemView.findViewById(R.id.childTextView)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyChildViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.child_item_layout, parent, false)
        return MyChildViewHolder(view)
    }

    override fun onBindViewHolder(holder: MyChildViewHolder, position: Int) {
        holder.textView.text = dataList[position]

    }

    override fun getItemCount(): Int {
        return dataList.size
    }
}
