import React from "react";
import {GoogleMap, withScriptjs, withGoogleMap} from "react-google-maps";

function Map() {
    return (
        <GoogleMap
            defaultZoom={10}
            defaultCenter={{lat: -34.397, lng: 150.644}}
        />
    )
}

const WrappedMap = withScriptjs(withGoogleMap(Map))

export default function ShopsMap() {
    return (
        <div style={{width: '100vw', height: '50vh'}}>
            <WrappedMap
                googleMapURL="https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=AIzaSyAU0_1-g0ZZOOOT3YmVL-UI2RVyoLVnJHM"
                loadingElement={<div style={{height: `100%`}}/>}
                containerElement={<div style={{height: `100%`}}/>}
                mapElement={<div style={{height: `100%`}}/>}
            />
        </div>
    )
}