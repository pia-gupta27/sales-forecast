import React, { useState, useEffect } from 'react';
import { ChakraProvider, Link, Box, Text, AspectRatio, HStack, Button, Spacer } from '@chakra-ui/react'; 

function Blogs() {
  return (
    <>
     <Box textAlign="center" paddingTop="40px" paddingBottom="40px">
        <Text fontSize="4xl" fontWeight="bold">Sales Forecasting Blogs</Text>
      </Box>

      <HStack spacing='24px' margin="18px">
      {/* <Box> */}
        <Box>
      <Button><Link href="https://hermitcrabs.io/blog/sales-forecasting-projection-prediction" target="_blank" rel="noopener noreferrer">View in Full Screen</Link></Button>
      {/*</Box> */}
      <AspectRatio width='480px' ratio={1}>
        <iframe
        title='1'
        src='https://hermitcrabs.io/blog/sales-forecasting-projection-prediction'
        />
      </AspectRatio>
      </Box>

      <Box>
      <Button><Link href="https://blog.salesflare.com/sales-forecasting" target="_blank" rel="noopener noreferrer">View in Full Screen</Link></Button>
      <AspectRatio width='480px' ratio={1}>
        <iframe
        title='1'
        src='https://blog.salesflare.com/sales-forecasting'
        />
      </AspectRatio>
      </Box>

      <Box>
      <Button><Link href="https://monday.com/blog/crm-and-sales/sales-prediction/" target="_blank" rel="noopener noreferrer">View in Full Screen</Link></Button>
      <AspectRatio width='480px' ratio={1}>
        <iframe
        title='1'
        src='https://monday.com/blog/crm-and-sales/sales-prediction/'
        />
      </AspectRatio>
      </Box>

      </HStack>
</>
  );
}

export default Blogs;
