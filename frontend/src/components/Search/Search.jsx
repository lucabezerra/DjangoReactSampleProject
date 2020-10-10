import React, { useState, useRef } from 'react';
import styled from 'styled-components';

import Button from '../Button';

import ResultItem from './ResultItem';

const Container = styled.div`
  display: flex;
  justify-content: center;
  flex-direction: column;
  width: 50%;
  margin: 0 auto;
`;

const Header = styled.div`
  display: flex;
  justify-content: center;
  flex-direction: column;
`;

const Title = styled.h1`
  align-self: center;
`;

const SearchContainer = styled.div`
  align-self: center;
`;

const StyledInput = styled.input`
  font-size: 16px;
`;

const ResultsSummary = styled.div`
  margin: 10px 0;
  text-align: center;
  ${props => props.color && 'background-color: ' + props.color + ';'}
  line-height: 2em;
  border-radius: 10px;
`;

const ResultsList = styled.div`
  display: flex;
  flex-direction: column;
`;


const Search = () => {
  const [results, setResults] = useState(null);
  const [totalResults, setTotalResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState();
  const textField = useRef(null);
  let resultString = null;

  const submitSearch = () => {
    const query = textField.current.value || '';
    setLoading(true);
    setResults(null);
    setTotalResults(0);
    setError(null);
    fetch(`http://localhost:8000/videos/search/?s=${query}`)
      .then(response => {
        response.json().then(responseData => {
          if (responseData.Response === "True") {
            setResults(responseData.Search);
            setTotalResults(responseData.totalResults);
          } else if (responseData.Error === "Too many results.") {
            setTotalResults(Number.MAX_SAFE_INTEGER);
          } else if (responseData.Error === "Movie not found.") {
            setTotalResults(0);
          }
          setLoading(false);
        });
      }).catch(err => {
        setError(err);
        setLoading(false);
      });
  }

  const onKeyPress = (e) => {
    if (e.key === 'Enter') {
      submitSearch();
    }
  }

  if (loading) {
    resultString = <ResultsSummary>Searching...</ResultsSummary>;
  } else if (error) {
    console.log(error);
    resultString = <ResultsSummary color="indianred">An error happened, please try again.</ResultsSummary>;
  } else if (totalResults === Number.MAX_SAFE_INTEGER) {
    resultString = <ResultsSummary color="papayawhip">Too many results were found, please narrow down your search.</ResultsSummary>;
  } else if (totalResults === 0) {
    resultString = <ResultsSummary color="papayawhip">No results found.</ResultsSummary>;
  } else if (totalResults > 0) {
    resultString = <ResultsSummary color="aquamarine"><b>{totalResults}</b> matches were found. See the first 10 hits below.</ResultsSummary>;
  }

  return (
    <Container>
      <Header>
        <Title>Search for Movies or TV Series</Title>
        <SearchContainer>
          <StyledInput type="text" ref={textField} onKeyPress={onKeyPress} />
          <Button text="Search" onClick={() => submitSearch()} />
        </SearchContainer>
      </Header>
      {resultString}
      <ResultsList>
        {results && results.map(item => <ResultItem key={item.imdbID} item={item} />)}
      </ResultsList>
    </Container>
  );
}

export default Search;
