import React from 'react';

const ImageDisplay = ({ imageUrl, altText }) => {
  return (
    <div>
      <img src={imageUrl} alt={altText} style={{ maxWidth: '100%' }} />
    </div>
  );
};

export default ImageDisplay;
