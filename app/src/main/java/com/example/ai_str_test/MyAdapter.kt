package com.example.ai_str_test

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.LinearLayout
import android.widget.TextView
import androidx.core.content.ContextCompat
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class MyAdapter(private val dataList: List<String>) : RecyclerView.Adapter<RecyclerView.ViewHolder>() {
    val childDataList = arrayListOf<String>()
    init{

        for (i in 1..20) {
            childDataList.add("Child Item $i")
        }
    }
    class MyViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val textView: TextView = itemView.findViewById(R.id.textView)
        val rv: RecyclerView = itemView.findViewById(R.id.child_rv)
    }
    class MyImageViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val imageView: ImageView = itemView.findViewById(R.id.imageView)
        val rv: RecyclerView = itemView.findViewById(R.id.child_rv)
    }

    class MyTitleSubtitleViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val subtitle: TextView = itemView.findViewById(R.id.subtitle)
        val title: TextView = itemView.findViewById(R.id.title)
        val rv: RecyclerView = itemView.findViewById(R.id.child_rv)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerView.ViewHolder {
        if(viewType == ViewHolderFactory.TYPE_0) {
            val view = LayoutInflater.from(parent.context).inflate(R.layout.item_layout, parent, false)
            return MyViewHolder(view)
        } else if(viewType == ViewHolderFactory.TYPE_1) {
            val view = LayoutInflater.from(parent.context).inflate(R.layout.item_layout2, parent, false)
            return MyTitleSubtitleViewHolder(view)
        }
        val view = LayoutInflater.from(parent.context).inflate(R.layout.item_layout1, parent, false)
        return MyImageViewHolder(view)
    }

    override fun onBindViewHolder(holder:  RecyclerView.ViewHolder, position: Int) {
        if(holder is MyViewHolder) {
            holder.textView.text = dataList[position]
            holder.rv.layoutManager = LinearLayoutManager(holder.rv.context, RecyclerView.HORIZONTAL, false)
            val adapter = MyChildAdapter(childDataList)
            holder.rv.adapter = adapter
        } else if(holder is MyImageViewHolder){
            holder.imageView.setImageResource( R.drawable.ic_launcher_background)
            holder.rv.layoutManager = LinearLayoutManager(holder.rv.context, RecyclerView.HORIZONTAL, false)
            val adapter = MyChildAdapter(childDataList)
            holder.rv.adapter = adapter
        } else if(holder is MyTitleSubtitleViewHolder){
            holder.title.text = dataList[position]
            holder.subtitle.text = dataList[position] + " subtitle"

            holder.rv.layoutManager = LinearLayoutManager(holder.rv.context, RecyclerView.HORIZONTAL, false)
            val adapter = MyChildAdapter(childDataList)
            holder.rv.adapter = adapter
        }


    }

    override fun getItemViewType(position: Int): Int {
        if(position % 3 == 0) return 0
        else if(position % 3 == 1) return 1
        return 2
    }

    override fun getItemCount(): Int {
        return dataList.size
    }
}
