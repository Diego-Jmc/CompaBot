import styles from "./page.module.css";
import Chat from "./chat/Chat";

export default function Home() {
  return (
    <main className={styles.main}>
      <div className="main-container">
      <Chat></Chat>
      </div>
    </main>
  );
}
