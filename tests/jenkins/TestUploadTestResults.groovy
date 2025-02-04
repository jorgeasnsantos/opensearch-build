import jenkins.tests.BuildPipelineTest
import org.junit.Before
import org.junit.Test

class TestUploadTestResults extends BuildPipelineTest {

    @Before
    void setUp() {

        this.registerLibTester(new UploadTestResultsLibTester( 'tests/jenkins/data/opensearch-1.3.0-build.yml', 'dummy_job', 123 ))

        super.setUp()
    }

    @Test
    void testUploadToS3() {
        super.testPipeline("tests/jenkins/jobs/UploadTestResults_Jenkinsfile")
    }
}
