function scrollto(id){
    element = document.getElementById(id)
    element.scrollIntoView({ behavior: "smooth", block: "start", inline: "nearest" });
    }


    function shownavbar(){
        sidebar = document.getElementById("sidebar")
        maincontent = document.getElementById("main-content")

        if (sidebar.style.display !== "block"){
        sidebar.style.display = "block"
        sidebar.style.width = "100%"
        maincontent.style.display = "block"
        } else {
        sidebar.style.display = ""
        sidebar.style.width = ""
        maincontent.style.display = ""
        }
    }