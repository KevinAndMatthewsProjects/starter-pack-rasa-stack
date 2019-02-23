import java.util.*;
public class HealthAdvice {
	private Random rand = new Random();
	public String getHealthAdvice() {
		String[] advice = new String[]{
			"Limit the amount sugary beverages you drink to prevent obesity and diabetes.",
			"Nuts have high nutritional value and can help you lose weight.",
			"Try to avoid processed junk food since they have low nutritional value.",
			"The US Department of Health and Human Services recommends at least 150 minutes of "
			+ "moderate aerobic activity or 75 minutes of vigorous aerobic activity a week, or"
			+ "a combination of the two."
		};
		return advice[rand.nextInt(advice.length)];
	}
	
	public static void main(String[] args) {
		HealthAdvice health = new HealthAdvice();
		System.out.println(health.getHealthAdvice());
	}
}
