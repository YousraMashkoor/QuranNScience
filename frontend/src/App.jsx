import { Routes, Route } from "react-router-dom";
import { Fragment, Suspense, lazy } from "react";

import ButtonAppBar from "./components/AppBar";
import Loading from "./components/Loading";

import componentLoader from "./utils/componentLoader";

const Home = lazy(() => componentLoader(() => import("./routes/HomePage")));
const NotFound = lazy(() => componentLoader(() => import("./routes/NotFound")));

function App() {
  return (
    <Fragment>
      <ButtonAppBar />
      <Suspense fallback={<Loading />}>
        <Routes>
          {/* public routes with no authentication */}
          <Route path="/" element={<Home />} />

          <Route path="*" element={<NotFound />} />
        </Routes>
      </Suspense>
    </Fragment>
  );
}

export default App;
