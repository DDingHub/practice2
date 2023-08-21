import axios from "axios";
import MakeTeamButton from "./MakeTeamButton";
import TeamCard from "./TeamCard";
import { useState, useEffect } from "react";
import Modal from "../../../Modal";
import ModalPortals from "../../../ModalPortals";
import "./Teams.css";
import "./TeamCard.css";
import TeamPage from "./TeamPage";
import MakeTeam from "./MakeTeam";

const Teams = ({ pageID, user }) => {
  const [teamData, setTeamData] = useState([]);
  const [contestData, setContestData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [modal, setModal] = useState(false);
  const [teamModal, setTeamModal] = useState(false);

  const handleModalShow = (status) => {
    setModal(status);
  };
  const handleTeamModalShow = (status) => {
    setTeamModal(status);
  };
  // useEffect(() => {
  //   window.location.reload();
  //   setTeamMake(!teamMake);
  // }, [teamMake]);

  useEffect(() => {
    async function getTeamData() {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/${pageID + 1}/`
        );
        setTeamData(response.data.teams);
        setContestData(response.data.contest);
        setLoading(false);
      } catch (error) {
        throw new Error("Error fetching data:", error);
      }
    }
    if (loading) {
      getTeamData();
    }
  }, [loading]);

  const makePost = () => {
    const posts = [];
    if (!teamData) {
      return posts;
    }
    //나열해서 보여주기 위한 foreach
    teamData.forEach((item) => {
      //   let day = item.application_period;
      //   day = day.substring(day.indexOf("D"));
      console.log("아이템임" + JSON.stringify(item));
      let post = {
        dev_capacity: item.dev_capacity,
        plan_capacity: item.plan_capacity,
        design_capacity: item.design_capacity,
        name: item.name,
        teamname: item.teamname,
        call: item.call,
        detail: item.detail,
        // dev: item.dev,
        // plan: item.plan,
        // design: item.design,
        // contest: item.contest,
        // user: item.user,
      };
      console.log("team낱개로보여주기" + JSON.stringify(post));
      console.log("받아온 팀데이터입니다" + JSON.stringify(teamData));
      console.log("받아온 콘테스트데이터입니다" + JSON.stringify(contestData));
      posts.push(post);
    });

    return posts;
  };
  const teams = makePost();
  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="teamContainer">
      {teams.map((team) => (
        <TeamCard
          key={team.id}
          {...team}
          handleTeamModalShow={handleTeamModalShow}
        />
      ))}
      <MakeTeamButton handleModalShow={handleModalShow} />
      <ModalPortals>
        <Modal
          contents={
            <MakeTeam
              pageID={pageID}
              user={user}
              handleModalShow={handleModalShow}
            />
          }
          show={modal}
          handleModalShow={handleModalShow}
        />
      </ModalPortals>
      <ModalPortals>
        <Modal
          contents={<TeamPage />}
          show={teamModal}
          handleModalShow={handleTeamModalShow}
        />
      </ModalPortals>
    </div>
  );
};

export default Teams;
