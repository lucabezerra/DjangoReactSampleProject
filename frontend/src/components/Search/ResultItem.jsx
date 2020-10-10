import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

import Button from '../Button';
import { capitalize } from '../../helpers/utils';


const Container = styled.div`
  display: flex;
  align-self: center;
  margin: 5px 0;
`;

const Poster = styled.img`
  width: 90px;
  height: 135px;
  object-fit: cover;
`;

const TextContainer = styled.div`
  display: flex;
  flex-direction: row;
  align-self: center;
  width: 300px;
`;

const AddButton = styled(Button)`
  height: 3em;
  margin-left: 10px;
  align-self: center;
`;

const ResultItem = ({ item }) => {
  const addToList = (item) => {
    fetch("http://localhost:8000/videos/video/", {
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      method: "POST",
      body: JSON.stringify({
        imdb_id: item.imdbID,
        category: item.Type,
        user: 1,
      }),
    }).then(response => {
      response.json().then(responseData => {
        console.log(':::: responseData:', responseData);
      });
    }).catch(err => {

    });
  }

  return (
    <Container>
      <a href={`https://www.imdb.com/title/${item.imdbID}/`} target="_blank">
        <Poster src={item.Poster} />
      </a>
      <TextContainer>
        <ul>
          <li><b>Title:</b> {item.Title}</li>
          <li><b>Year:</b> {item.Year}</li>
          <li><b>Type:</b> {capitalize(item.Type)}</li>
        </ul>
      </TextContainer>
      <AddButton text="Add to My List" onClick={() => addToList(item)} />
    </Container>
  );
};

ResultItem.propTypes = {
  item: PropTypes.object.isRequired,
}

export default ResultItem;
