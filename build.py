import hudson.plugins.timestamper.api.TimestamperAPI;
import java.io.BufferedReader;

String = "time=HH:mm:ss";
try (BufferedReader reader = TimestamperAPI.get().read(build, query)) {
    // read timestamps here
}
