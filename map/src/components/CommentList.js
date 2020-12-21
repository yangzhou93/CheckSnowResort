import React from 'react';
import { ListGroup, ListGroupItem,Button } from 'reactstrap';

export default function CommentList({comments,handleLikeComment}) {
  return (
    <div>
      <h2>comments:</h2>
      <ListGroup>
      {comments && comments.map((comment, index) => (
        <ListGroupItem>
          <span>{comment.body} <Button onClick = {()=>{handleLikeComment(comment.id)}} >like {comment.likes}</Button></span>
        </ListGroupItem>
      ))}
    </ListGroup>
    </div>
    
  )
}