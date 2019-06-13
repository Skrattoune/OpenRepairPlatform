let inputSelector = "#id_address";

let addressesToCoordinates = {};

function addrSelected(event, addr, item) {
    let longitude = document.getElementById("id_longitude");
    let latitude = document.getElementById("id_latitude");
    longitude.value = addressesToCoordinates[addr].longitude;
    latitude.value = addressesToCoordinates[addr].latitude;
}

function addressFound(f) {
    addressesToCoordinates[f.properties.label] = {
        longitude: f.geometry.coordinates[0],
        latitude: f.geometry.coordinates[1],
    };
}
