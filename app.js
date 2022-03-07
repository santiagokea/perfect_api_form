function set_active_tab(tab_id){
  document.querySelectorAll("#left_panel #tabs > a").forEach(tab=>{
    tab.classList.remove("text-blue")
  })
  document.querySelector(`#${tab_id}`).classList.add("text-blue")
}

set_active_tab("home")