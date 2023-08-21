const countCharacters = (arr, targetChars) => {
  const charCounts = {};

  // 각 문자의 개수를 세어서 charCounts 객체에 저장
  for (const char of targetChars) {
    charCounts[char] = arr.filter((item) => item === char).length;
  }

  return charCounts;
};
export default countCharacters;
