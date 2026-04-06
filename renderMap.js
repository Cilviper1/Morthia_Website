// PAGE ELEMENTS
const closeBtn = document.querySelector(".close-btn");
const sidebarContainer = document.querySelector(".sidebar-container");
const sidebarContent = document.querySelector(".sidebar-content");
const wrapper = document.querySelector(".wrapper-home");

async function loadPlaceInfo() {
  const res = await fetch('../Morthia/places.json')
  return res.json()
}

// Opens sidebar and populates it with place info

function getInfo(info) {
  sidebarContent.innerHTML = "";

  const Header = document.createElement("h3");
  Header.innerHTML = info.place;
  sidebarContent.appendChild(Header);

  if (info.leader) {
    const Leader = document.createElement("h4");
    Leader.innerHTML = info.leader;
    sidebarContent.appendChild(Leader);
  }

  if (info.description) {
    const Content = document.createElement("p");
    Content.innerHTML = info.description;
    sidebarContent.appendChild(Content);
  }

  sidebarContainer.classList.remove("collapsed");
  wrapper.classList.add("sidebar-open");
}

function collapseSidebar() {
  sidebarContainer.classList.add("collapsed");
  wrapper.classList.remove("sidebar-open");
}

// Close button collapses instead of clearing
closeBtn.addEventListener("click", collapseSidebar);

// Start collapsed — sidebar opens on first click
collapseSidebar();

// Leaflet
async function renderMap(imgPath, mapHeight, mapWidth) {
  const placesInfo = await loadPlaceInfo()

  var map = L.map("map", {
    crs: L.CRS.Simple,
    minZoom: -5,
    maxZoom: 0.5,
    zoomSnap: 0.5,
    attributionControl: false,
  });

  var bounds = [
    [0, 0],
    [mapHeight, mapWidth],
  ];

  var image = L.imageOverlay(imgPath, bounds).addTo(map);
  map.fitBounds(bounds);
  image.getElement().style.boxSizing = "border-box";

  for (const placeInfo of Object.values(placesInfo)) {
    if (placeInfo.coords) {
      L.polygon(placeInfo.coords, { color: 'transparent', fillOpacity: 0 })
        .on('click', () => getInfo(placeInfo))
        .on('mouseover', function () { this.setStyle({ fillColor: '#fff', fillOpacity: 0.15 }) })
        .on('mouseout', function () { this.setStyle({ fillOpacity: 0 }) })
        .addTo(map)
    }
  }
}
