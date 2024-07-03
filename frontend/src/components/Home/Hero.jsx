import {
    Box,
    Button,
    Flex,
    Image, 
    Spacer,
    Text,
    useMediaQuery,
  } from '@chakra-ui/react';
  import React from 'react';
  import Sales_Pic from '../../assets/sales_pic.png'
  const Hero = () => {
    const [isLargerThanLG] = useMediaQuery('(min-width: 62em)');
    return (
      <Flex
        alignItems="center"
        w="full"
        px={isLargerThanLG ? '16' : '6'}
        py="16"
        minHeight="90vh"
        justifyContent="space-between"
        flexDirection={isLargerThanLG ? 'row' : 'column'}
      >
        <Box mr={isLargerThanLG ? '6' : '0'} w={isLargerThanLG ? '60%' : 'full'}>
          <Text
            fontSize={isLargerThanLG ? '5xl' : '4xl'}
            fontWeight="bold"
            mb="4"
          >
            {' '}
            Sales Predictor
          </Text>
  
          <Text mb="6" fontSize={isLargerThanLG ? 'lg' : 'base'} opacity={0.7}>
            Predict the sales of your business using our machine learning model. 
          </Text>
  
          <Button
            w="200px"
            colorScheme="blue"
            variant="solid"
            h="50px"
            size={isLargerThanLG ? 'lg' : 'md'}
            mb={isLargerThanLG ? '0' : '10'}
          >
            <a target="_blank" rel="noreferrer" href="/signin">
              Predict
            </a>
          </Button>
        </Box>
        <Spacer />
        <Flex
          w={isLargerThanLG ? '40%' : 'full'}
          alignItems="center"
          justifyContent="center"
        >
          <Image src={Sales_Pic} alt="Sales" />
        </Flex>
      </Flex>
      
    );
  };
  
  export default Hero;