import React from "react";

const Home = () => {
  return (
    <React.StrictMode>
      <div className="main-page-content">
        <div id="home">
          <div id="particles-js"></div>
          <div className="home-content-main">
            <div className="table-cell">
              <div className="container">
                <div className="row home-row">
                  <div className="col-md-12 col-sm-12">
                    <div className="home-text wow fadeIn text-center">
                      <h1 className="cd-headline clip is-full-width">
                        <span
                          className="cd-words-wrapper"
                          style={{ width: "266px", overflow: "hidden" }}
                        >
                          <b className="is-hidden">Li Junru</b>
                          <b className="is-hidden">Respiratory Diseases</b>
                          <b className="is-visible">Developer</b>
                        </span>
                      </h1>
                      
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="parallax" data-velocity="-.1"></div>
          <div className="parallax" data-velocity="-.5" data-fit="525"></div>
        </div>

        {/* <!-- ================================ ABOUT =============================== --> */}

        <div id="about">
          <div className="about-content">
            <div className="love-grid text-center">
              <div className="container">
                <div className="row">
                  <div className="col-md-12">
                    <div className="main-title text-center wow fadeIn">
                      <h3>What I do</h3>
                      <div className="underline1"></div>
                      <div className="underline2"></div>
                      <p>
                        呼吸疾病是一类严重影响人类健康的疾病，包括哮喘、慢性阻塞性肺疾病（COPD）、肺癌等多种疾病。随着人口老龄化和环境污染的日益严重，呼吸疾病的发病率和死亡率呈上升趋势，给个人和社会带来了巨大的负担。因此，建立一个有效的呼吸病知识库和查询平台，对于提高呼吸疾病的早期诊断、治疗和管理具有重要的意义。
目前，虽然有大量的医学文献和临床指南可供参考，但呼吸疾病的知识分散、碎片化，且难以系统地应用于临床实践。传统的呼吸疾病诊断主要依赖于医生的经验和临床判断，但这种方式容易受主观因素和个体差异的影响，导致诊断的准确性和一致性存在较大的局限性。因此，设计和实现一个呼吸病知识库和查询平台，可以为医生和患者提供准确、系统、实时的呼吸疾病信息，辅助临床决策和治疗方案的制定。
本课题的意义在于通过构建呼吸病知识库，将分散的呼吸疾病知识进行整合和标准化，为医生提供一个可靠的参考资源，帮助其做出更准确的诊断和治疗决策。同时，查询平台的设计与实现，使得患者能够便捷地获取与呼吸疾病相关的信息，提高患者的健康管理和自我诊断能力。此外，该平台还可为医学教育和研究提供支持，促进呼吸疾病领域的学术交流和知识共享。
通过本研究的成果，可以提高呼吸疾病的早期筛查和诊断准确性，减少误诊和漏诊的风险，优化医疗资源的利用，降低医疗成本，改善患者的生活质量。同时，该平台也可以为患者提供有关呼吸病的知识和诊疗建议，帮助患者更好地了解和管理自己的健康状况。本研究的成果具有一定的推广应用价值，对于医学领域的知识库和查询平台的设计与实现具有借鉴意义。

                      </p>
                    </div>
                  </div>
                </div>
                <div className="row love-row wow fadeIn">
                  <div className="col-md-3 col-sm-6">
                    <div className="love-details" data-wow-delay=".1s">
                      <i
                        className="fa fa-pencil-square-o love-icon"
                        aria-hidden="true"
                      ></i>
                      <h3>修改诊断路径</h3>
                      <div className="underline1"></div>
                      <div className="underline2"></div>
                      <p>You can edit the knowledge base</p>
                    </div>
                  </div>
                  <div className="col-md-3 col-sm-6">
                    <div className="love-details" data-wow-delay=".3s">
                      <i
                        className="fa fa-file-image-o love-icon"
                        aria-hidden="true"
                      ></i>
                      <h3>输入病历信息</h3>
                      <div className="underline1"></div>
                      <div className="underline2"></div>
                      <p>You can enter your medical record to get the diagnosis result</p>
                    </div>
                  </div>
                  <div className="col-md-3 col-sm-6">
                    <div className="love-details" data-wow-delay=".2s">
                      <i
                        className="fa fa-globe love-icon"
                        aria-hidden="true"
                      ></i>
                      <h3>查看诊断结果</h3>
                      <div className="underline1"></div>
                      <div className="underline2"></div>
                      <p>Your can check your diagnosis result</p>
                    </div>
                  </div>
                  <div className="col-md-3 col-sm-6">
                    <div className="love-details" data-wow-delay=".4s">
                      <i className="fa fa-cog love-icon" aria-hidden="true"></i>
                      <h3>查看历史记录</h3>
                      <div className="underline1"></div>
                      <div className="underline2"></div>
                      <p>You can view the history to review your medical record and dignosis result</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div className="about-back"></div>
            {/* <div className="me-grid">
              <div className="container">
                <div className="row">
                  <div className="col-md-4 col-sm-6 col-xs-12 about-col">
                    <div className="about-image">
                      <img
                        src="assets/img/about-image.jpg"
                        alt="sanajit-jana"
                        className="about-img wow fadeIn"
                      />
                    </div>
                  </div>
                  <div className="col-md-8 col-sm-6 col-xs-12 about-col">
                    <div className="about-details wow fadeIn">
                      <div className="main-title left-title text-left wow fadeIn">
                        <h3>Hello! This is Sanajit</h3>
                        <div className="underline1 no-margin"></div>
                        <div className="underline2 no-margin"></div>
                      </div>
                      <p className="wow fadeIn">
                        I am a web developer from Kolkata, India. I enjoy
                        building everything from small business sites to rich
                        interactive web apps. if you are a business seeking a
                        web presence or an employer looking to hire, you can get
                        in touch with me{" "}
                        <a className="underline2" href="#contact">
                          {" "}
                          here.
                        </a>{" "}
                        I design and build digital products with simple and
                        beautiful code. I specialize in custom web theme
                        development and love what I do.
                        <br />
                        <br />
                        Since beginning my journey as a web developer in my
                        college days, I've done remote work for agencies,
                        consulted for startups, and collaborated with talented
                        people to create digital products for both business and
                        consumer use. I'm quietly confident, naturally curious,
                        and perpetually working on improving my chops one design
                        problem at a time.
                      </p>
                      <a
                        className="about-link-1"
                        href="assets/cv/sanajit-jana-profile.pdf"
                        target="_blank"
                      >
                        See Resume
                      </a>
                      <a className="about-link-2" href="#contact">
                        Hire Me
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="work-counter text-center">
              <div className="counter">
                <div className="container">
                  <div className="row wow fadeIn">
                    <div className="col-md-3 col-sm-6">
                      <div className="work-statistics">
                        <i
                          className="fa fa-pencil-square-o stat-icon"
                          aria-hidden="true"
                        ></i>
                        <h3 className="Count">0021</h3>
                        <div className="underline1"></div>
                        <div className="underline2"></div>
                        <p>Web Design Completed</p>
                      </div>
                    </div>
                    <div className="col-md-3 col-sm-6">
                      <div className="work-statistics">
                        <i
                          className="fa fa-crop stat-icon"
                          aria-hidden="true"
                        ></i>
                        <h3 className="Count">0040</h3>
                        <div className="underline1"></div>
                        <div className="underline2"></div>
                        <p>UI/UX Design Done</p>
                      </div>
                    </div>
                    <div className="col-md-3 col-sm-6">
                      <div className="work-statistics">
                        <i
                          className="fa fa-bolt stat-icon"
                          aria-hidden="true"
                        ></i>
                        <h3 className="Count">0015</h3>
                        <div className="underline1"></div>
                        <div className="underline2"></div>
                        <p>Website Created</p>
                      </div>
                    </div>
                    <div className="col-md-3 col-sm-6">
                      <div className="work-statistics">
                        <i
                          className="fa fa-coffee stat-icon"
                          aria-hidden="true"
                        ></i>
                        <h3 className="Count">0085</h3>
                        <div className="underline1"></div>
                        <div className="underline2"></div>
                        <p>Cups Coffee Taken</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div> */}
          </div>
        </div>

        {/* <!-- ================================ Skill =============================== --> */}

        
         
        

        

        

        

        
        

        {/* <!-- ================================ CONTACT ========================== --> */}

        
      </div>
    </React.StrictMode>
  );
};

export default Home;
