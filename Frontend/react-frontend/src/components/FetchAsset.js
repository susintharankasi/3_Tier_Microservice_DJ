import React from 'react';

const FetchAsset = ({ assets }) => {
  return (
    <div>
      <h3>Asset List</h3>
      <ul>
        {assets.map(asset => (
          <li key={asset.id}>{asset.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default FetchAsset;
