import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import { ChakraProvider } from '@chakra-ui/react'
import Signin from './components/Signin';
import Signup from './components/Signup';
import Home from './components/Home';
import Sales from './components/Sales';
import Blogs from './components/Blogs';

function App() {
  return (
    <ChakraProvider>
    <div className="App">
      <Router>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/signin' element={<Signin />} />
          <Route path='/signup' element={<Signup />} />
          <Route path='/sales' element={<Sales />} />
          <Route path='/blogs' element={<Blogs />} />
        </Routes>
      </Router>
  </div>
  </ChakraProvider>
  );
}

export default App;