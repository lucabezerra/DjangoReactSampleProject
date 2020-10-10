import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';


const StyledInput = styled.input`
  background: darkcyan;
  color: white;
  border-radius: 5px;
  font-weight: bold;
  font-size: 16px;
  margin: 10px;
`;

export const Button = (props) => (
  <StyledInput type="button" value={props.text} {...props} />
);

Button.propTypes = {
  text: PropTypes.string.isRequired,
};

export default Button;