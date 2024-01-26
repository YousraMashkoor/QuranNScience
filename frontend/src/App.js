import { Routes, Route } from "react-router-dom";
import { Fragment, Suspense, lazy } from "react";

import ButtonAppBar from "./components/AppBar/index";
import Loading from "./components/Loading";

const Home = lazy(() => import("./routes/HomePage/index"));

function App() {
  return (
    <Fragment>
      <ButtonAppBar />
      <Suspense fallback={<Loading />}>
        <Routes>
          <Route index path="/" element={<Home />} />
        </Routes>
      </Suspense>
    </Fragment>
  );
}

export default App;
