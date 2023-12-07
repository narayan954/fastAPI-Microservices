import {BrowserRouter, Route, Routes} from 'react-router-dom';

import Orders from './components/orders';
import Products from "./components/Products";
import ProductsCreate from "./components/CreateProducts";

function App() {
    return <BrowserRouter>
        <Routes>
            <Route path="/" element={<Products/>}/>
            <Route path="/create" element={<ProductsCreate/>}/>
            <Route path="/orders" element={<Orders/>}/>
        </Routes>
    </BrowserRouter>;
}

export default App;