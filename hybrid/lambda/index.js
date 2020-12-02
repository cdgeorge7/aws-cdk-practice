exports.handler = async (event) => {
  console.log("event: ", JSON.stringify(event, null, 2));
  return {
    statusCode: 200,
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
    body: JSON.stringify({
      message: "toots mcgoots",
    }),
  };
};
