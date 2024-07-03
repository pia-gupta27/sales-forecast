import {useEffect} from 'react';

const Sales = () => {
  useEffect(() => {
    window.location.href = 'http://localhost:3000';
  }, []);

  return null; 
};

export default Sales;
