import Promise from "./components/Promise";
import NavigationBar from "./components/Navbar";
import ShopsMap from "./components/GoogleMap";

function App(){
  return(
      <>
      <NavigationBar/>
      <Promise/>
      <ShopsMap/>
      </>
  )
}
export default App;