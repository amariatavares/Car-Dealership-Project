import { Routes, Route } from "react-router-dom";

import LoginPanel from "./components/Login/Login"
import RegisterPanel from "./components/Register/Register";
import DealersPanel from "./components/Dealers/Dealers"
import DealerPanel from "./components/Dealers/Dealer"
import PostReview from "./components/Dealers/PostReview"

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<RegisterPanel />} />
      <Route path="/dealers" element={<DealersPanel />} />
      <Route path="/dealer/:id" element={<DealerPanel />} />
      <Route path="/postreview/:id" element={<PostReview/>} />
    </Routes>
  );
}
export default App;
