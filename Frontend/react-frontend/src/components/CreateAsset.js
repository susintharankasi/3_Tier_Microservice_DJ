import React, { useState } from 'react';

const CreateAsset = ({ onCreate }) => {
  const [assetName, setAssetName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onCreate({ name: assetName });
    setAssetName('');
  };

  return (
    <div>
      <h3>Create New Asset</h3>
      <form onSubmit={handleSubmit}>
        <input 
          type="text"
          placeholder="Enter asset name"
          value={assetName}
          onChange={(e) => setAssetName(e.target.value)}
        />
        <button type="submit">Add Asset</button>
      </form>
    </div>
  );
};

export default CreateAsset;
