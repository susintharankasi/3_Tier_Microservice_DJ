import React from 'react';

function UserList({ users, onDelete }) {
  return (
    <div className="user-list">
      <h3>Existing Users</h3>
      {users.length === 0 ? (
        <p>No users found.</p>
      ) : (
        <ul>
          {users.map(user => (
            <li key={user.id}>
              <div>
                <strong>{user.name}</strong> <br />
                <span>{user.email}</span>
              </div>
              <button onClick={() => onDelete(user.id)}>Delete</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default UserList;
