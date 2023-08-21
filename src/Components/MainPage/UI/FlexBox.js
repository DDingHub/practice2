import "./FlexBox.css";
export const FlexBox = ({ dir, children }) => {
  return (
    <div className="FlexBox" style={{ flexDirection: `${dir}` }}>
      {children}
    </div>
  );
};
