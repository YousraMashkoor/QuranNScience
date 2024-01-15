import {Routes, Route} from 'react-router-dom';
import { Fragment } from 'react';

import ButtonAppBar from './components/AppBar/AppBar';
import Home from './routes/HomePage/Home';

function App() {
  return (
    <Fragment>
      <ButtonAppBar/>
      <Routes>
        <Route index path="/" element={<Home/>}/>
      </Routes>
    </Fragment>
  );
}

export default App;
