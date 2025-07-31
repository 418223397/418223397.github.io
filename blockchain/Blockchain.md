### Blockchain: 

#### Definition:

is the kind of distributed ledger technology(DLT) that helps people do business with each other by tracking who owns what. For people to do business with one another, we need: Trust, Transparency and Auditability/verifiability.

#####  Unique:  

##### solving double-payment(双花问题) problem by the first miner to find the truth to tell the everyone. 

- ##### each block contains: data + Hash(like fingerprint) + Hash of previous block ( 1st block is genesis block) e.g. P2P network



#### Basic Concepts:

1. Shared/distributed Ledger Technology:(分布式账簿技术) 

   Each participant in the business transaction has a copy of the source of truth, which cannot be manipulated. All copies are up-to-date and consistent with one another, eliminating the need for a third party to hold the source of truth. 

   - “回避”了拜占庭将军问题：Byzantine Generals Problem: 分布式对等网络通信容错问题：
   - 区块链技术只是分布式账簿技术的一个分支而已。

   

2. cryptography:

   Identify of participants involved in a transaction and to verify those transactions by public/private key encryption technology. 

   

3. Consensus/Trust  Mechanism:

   The blockchain system provides an agreed-upon protocol that allows all participants to decide on the order of the transactions in the ledger. Trust on without a third-party organization with the trust in transaction.

   - Bitcoin: 共识算法 PoW (proof of Work, 工作量证明机制)；无法支撑公链的需求
   - ETH：权益类证明 PoS  (proof of stake，持有量证明机制)
   - EOS: dPoS (delegated proof of stake): 持有量和持有时间证明机制， 基于投票选举的共识算法，持币者选出若干个节点来运营网络；目前公链最靠谱选择之一

   

4. Smart Contracts

   The transaction execution automatedly with the computer functions. 
   
   - how to write smart contracts: using **Solidity** (```.sol```) programming language on VsCode. 
   - firstly , initialize a Node project. 
   - compile a Solidity Smart Contract Using Node.js



#### Career Opportunities in Blockchain

1. Blockchain Core Developer:

   - building the blockchain architecture and protocol, distributed ledger technology
   - Golang, C++, Java

2. Blockchain Software Developer(Blockchain dApp)

3. Front-End Developer (前端开发)

   - experience with JavaScript(ES6)
   - React.JS on production-ready application
   - understand Redux and Trunk or Saga
   - experience with REST APIs and TypeScript
   - Understand UX/UI
   - Full stack JavaScript : 

4. Back-End developer

   - experience with JavaScript(ES6), Node.js, Express.js
   - database: PostgreSQL, MySQL

5.  QA Engineer: (Quality Assurance)

   - understand the blockchain product works
   - writing **automated** tests for dApp and website: JS with Protractor, and Selenium with C or Java
   - Rally and HP ALM for test management
   - Automating the testing of mobile application using Appium
   - Agile using tools: Rally or Jira
   - Performance/load testing tools: Balze Meter and jMeter
   - TDD frameworks: Cucumber
   - CRAFT: Client-Ready Automation Framework for Testing (regression automation framework for testing)

   - best ways to get full test coverage of the product



### 1. 为什么要学习区块链

- 区块链仍然很早期
- 这个领域还没有很强的人才漏斗
  - 不是目前就业的主流：机器学习，网络编程或游戏开发
  - 属于cyberpunk/cryptopunk
- 大部分创新都发生在学术界之外
  - 白皮书，博客，公共休闲频道，开源软件
- 加密货币真的很酷吗
  - Naval Ravikant

### 2. 预备知识

- 计算机科学

  - 数据结构：特性和复杂性
    - linked lists
    - binary search trees
    - hash maps
    - graphs(特别是在区块链中具有显著特征的有向非循环图)
  - 密码学
    - 加密货币：公钥/私钥（public/private key cryptography) 作为身份和身份验证
    - 学习建议：RSA => ECDSA => 椭圆曲线密码
    - 另一个密码原语：密码散列函数（哈希函数）：可用于承诺机制，是merkle树的构建块。
    - merkle trees支持Merkle proofs,这是区块链用于可扩展性的关键优化之一
  - 分布式系统
    - 一旦系统不再运行在一台机器上，就必须开始论证一致性和共识：可线性化 vs. 最终一致性模型；容错一致性算法的保证 （e.g. Paxos 和 Raft)
    - 分布式系统中论证时间的困难；安全 vs. 活性
    - 理解拜占庭容错共识的难点：这是公共区块链的主要安全要求， 了解PBFT(这个是首个提供拜占庭容错共识的可扩展算法之一)的总体思路及其安全性保障机制
    - 理解传统的分布式数据库（其核心是区块链本质上是数据库）
      - 分片（通过一致性哈希）
      - 主从复制（leader-follower replication)
      - 分布式哈希表(DHTs): e.g. Chord 或 Kademlia
  - 网络
    - 区块链的分布式在很大程度上：点对点网络拓扑结构
      - blockchain=P2P网络的直接产物
      - 了解区块链通信模型：
        - TCP 和 UDP
        - 数据包模型
        - IP数据包
      - 公共区块链
        - 通过gossip protocols 和flooding传播
        - P2P网络设计的历史：Napster to Gnutella, BitTorrent, Tor

- 经济学：crypto通过其经济结构获得许多安全属性-加密经济学

- 博弈论： 研究多个主体之间的收益和激励。

  - 博弈论分析的基本工具
  - 分析一次性和持续性游戏中的激励因素
  - 纳什均衡点：非合作博弈均衡
  - 谢林点： Schelling Points

- 宏观经济学

  - 加密货币：不仅是协议，也是一种货币形式
  - 响应宏观经济规律
  - 加密货币受制于不同的货币政策，并对通货膨胀和通货紧缩作出可预见的反应。
  - 货币的流通速度

- 微观经济学

  - 加密货币与市场交织在一起，供求曲线

  - 竞争与机会成本

  - 硬币发行和密码经济系统中：拍卖理论

    

### 3. 为什么要学区块链开发

- 2008年 Satoshi的比特币（协议）：
  - 工作证明
  - 分叉选择规则（中本共识）

### 4. 自己构建区块链

- 用各种编程语言，建立自己的区块链，并满足自己学习的要求 （Ruby, Python)
- 掌握如何在区块链（即比特币）上简单实现一个支付应用程序；就有足够的背景能够阅读和理解比特币的白皮书
- 比特币挖矿经济学和机制：普林斯顿的比特币和加密货币课程中观看关于比特币挖矿的讲座
- 理解每一个组成部分的含义，能够玩比特币块浏览器和导航原始比特币交易



### 5. 以太坊（Ethereum)和智能合约的编程

- 智能合约：在虚拟机上运行程序名称
  - 创建自动执行的金融合约
- ICO
- Ethereum使用的是账户模型；Bitcoin是UTXO模型
- Ethereum的主要编程语言：Solidity-是静态类型的JavaScript-esque语言
  - Solidity 语言开发：cryptozombie courses
  - "hello world" in Ethereum可以创建一个兼容的ERC-20
  - Remix是一个浏览器内的Solidity编辑器和编译器-Ethereum开发的训练轮，可以承载接下来的训练练习
- 创建一个投票系统：Ethereum的Todo应用
  - Karl Floersch有一篇很赞的教程：如何搭建一个安全的委员会公开投票系统
  - middle way: 设计一个coin toss游戏。玩家在抛硬币上下注，如何防止玩家作弊？

### 6. 智能合约的安全:智能合约开发最重要的环节

- 三个攻击：

  - 一直受到灾难性黑客攻击，包括DAO黑客攻击
  - Parity钱包黑客攻击
  - 第二次Parity钱包黑客攻击

- 问题：

  - 程序员自身的bug
  - 前端集群 frontrunning
  - 安全生成随机性 secure generation of randomness
  - 增加安全保障：
    - OpenZeppelin的开源合约
    - Phil Daian: 优秀的智能合约黑客挑战：Hack this Contract

  #### 7. 从新手到老手：

  - VsCode/Atom作为文本编辑器：Solidity插件
  - Ganache: 为了与本地区块链进行交互
  - Truffle框架：基于JS测试和配置构建管道
  - IPFS: Juan Benet-对于Ethereum和IPFS的全节点的交互，大多数开发人员推荐Infura
    - Etherscan 和ETH Gas Station在以太网络上提供有用的实时统计数据
  - 建立了完整的Web3堆栈=>部署端对端Dapp
    - 后端提供了一个使用Node和Postgres的良好的全堆栈概览
    - IPFS作为持久性层（persistence layer）创建一个完全去中心的应用程序。

  #### 8.创建自己的项目

  - 好的起点：OpenZeppelin
  - 寻找一个好项目：从关注`Slack`和`Rocketcha`未解决的问题，主动提出来去帮忙

  

  #### 9. 领导区块链社区 （采用信息节食法）

  - podcast:

    - Software Engineering Daily Blockchain

    - twitter:  **建设者**，企业家，记者，交易员和“思想领袖”

      

  

  









