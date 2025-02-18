data class MasterView(
    val view: ViewData
)

data class ViewData(
    val title: String,
    val subtitle: String,  // New field added 💖
    val items: List<ItemData>,
    val type: String,
)

data class ItemData(
    val name: String
)
