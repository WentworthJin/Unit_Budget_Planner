// This method is for role identification
function myFunction() {
    var x = document.getElementById("role");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }
function reply_click(clicked_id)
{
    alert(clicked_id);
}