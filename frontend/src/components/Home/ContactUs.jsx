import {
    Flex,
    FormControl,
    Text,
    Input,
    Textarea,
    Button,
    useMediaQuery,
    useToast,
    Link
  } from '@chakra-ui/react';
  import React, {useState} from 'react';
  
  const ContactUs = () => {
    const [isLargerThanLG] = useMediaQuery('(min-width: 62em)');
    const toast = useToast();
  const [subject, setSubject] = useState('');
  const [body, setBody] = useState('');

    const submitForm = () => {
      const encodedSubject = encodeURIComponent(subject);
      const encodedBody = encodeURIComponent(body);
      const mailtoLink = `https://mail.google.com/mail/?view=cm&fs=1&to=anupriyalathey@gmail.com&su=${encodedSubject}&body=${encodedBody}`;
      window.open(mailtoLink, "_blank");

      return toast({
        title: 'Message sent!🚀',
        description: 'Thank you for contacting us!',
        status: 'success',
        duration: 9000,
        isClosable: true,
      });
    };



    return (
      <Flex
        id='contact'
        w="full"
        minHeight="90vh"
        py="16"
        px={isLargerThanLG ? '16' : '6'}
        alignItems="center"
        flexDirection="column"
        justifyContent="center"
      >
        <Text fontSize="3xl" mb="6">
          Contact Us
        </Text>
  
        <FormControl
          w={isLargerThanLG ? '60%' : 'full'}
          display="flex"
          flexDirection="column"
          alignItems="start"
        >
          <Input
            id="fullName"
            type="text"
            placeholder="Full Name"
            mb="5"
            h="14"
          />
  
          <Input id="email" type="email" placeholder="Email" mb="5" h="14" />
  
          <Input id="subject" value={subject} type="text" placeholder="Subject" mb="5" h="14" onChange={(e) => setSubject(e.target.value)}/>
  
          <Textarea id="body" value={body} placeholder="Enter a message" mb="5" rows={7} p="5" onChange={(e) => setBody(e.target.value)}/>

          <Button
            colorScheme="blue"
            size="lg"
            textAlign="left"
            width="200px"
            type="submit"
            onClick={submitForm}
          >
            SUBMIT
          </Button>

        </FormControl>
      </Flex>
    );
  };
  
  export default ContactUs;
  