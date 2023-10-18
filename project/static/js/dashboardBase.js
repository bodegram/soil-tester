console.log('hi')
let menuCard = document.getElementById("menu-card");
let sidebarMenu = document.getElementById('sidebar')
sidebarMenu.classList.add('sidebar-hide')

const menuCardClick = () => {
  menuCard.classList.toggle("hide");
};


const openSideMenu = () =>{
    sidebarMenu.classList.toggle('sidebar-hide')
}

