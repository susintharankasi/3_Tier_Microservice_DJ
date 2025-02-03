import React from 'react';

const DeleteAsset = ({ assets, onDelete }) => {
  return (
    <div>
      <h3>Delete Asset</h3>
      <ul>
        {assets.map(asset => (
          <li key={asset.id}>
            {asset.name}
            <button onClick={() => onDelete(asset.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DeleteAsset;
