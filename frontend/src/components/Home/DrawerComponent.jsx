import React from 'react';
import {
  Drawer,
  DrawerBody,
  DrawerHeader,
  DrawerOverlay,
  DrawerContent,
  DrawerCloseButton,
  Link,
  Flex,
} from '@chakra-ui/react';

const DrawerComponent = ({ isOpen, onClose, btnRef }) => {
  return (
    <Drawer
      isOpen={isOpen}
      placement="right"
      onClose={onClose}
      finalFocusRef={btnRef}
      zIndex="popover"
    >
      <DrawerOverlay />

      <DrawerContent>
        <DrawerCloseButton />
        <DrawerHeader>Sales Predictor</DrawerHeader>

        <DrawerBody>
          <Flex flexDirection="column">
            <Link mb="5">About</Link>
            <Link to="contact" spy={true} smooth={true} offset={-130} duration={900} style={{cursor: "pointer"}}>
              Contact Us
            </Link>
          </Flex>
        </DrawerBody>
      </DrawerContent>
    </Drawer>
  );
};

export default DrawerComponent;